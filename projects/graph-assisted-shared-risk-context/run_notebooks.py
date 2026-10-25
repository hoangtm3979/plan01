#!/usr/bin/env python3
"""Execute public thesis notebooks in separate fresh kernels and record real results."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

import nbformat

LABS = Path(__file__).resolve().parent
NOTEBOOKS = LABS / "notebooks"


def source_sha256(notebook):
    cells = [{"cell_type": cell.cell_type, "source": cell.source} for cell in notebook.cells]
    payload = json.dumps(cells, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def package_versions():
    packages = ["numpy", "pandas", "scipy", "scikit-learn", "matplotlib", "tensorflow-cpu",
                "tensorflow", "keras", "nbformat", "nbclient", "ipykernel", "jupyter-client"]
    versions = {}
    for package in packages:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            pass
    return versions


def inprocess_worker(path, result_path, in_place):
    """Use a real IPython in-process kernel in a dedicated OS process, without sockets."""
    from ipykernel.inprocess.manager import InProcessKernelManager

    started = time.monotonic()
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    result = {
        "notebook": path.name, "source_sha256": source_sha256(notebook),
        "code_cells": sum(c.cell_type == "code" and bool(c.source.strip()) for c in notebook.cells),
        "status": "FAIL", "executed_code_cells": 0,
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    manager = InProcessKernelManager()
    client = None
    try:
        os.chdir(NOTEBOOKS)
        manager.start_kernel()
        manager.kernel.shell.run_line_magic("matplotlib", "inline")
        client = manager.client()
        client.start_channels()
        for cell in notebook.cells:
            if cell.cell_type == "code":
                cell.execution_count = None
                cell.outputs = []
                cell.metadata.pop("execution", None)
        for index, cell in enumerate(notebook.cells):
            if cell.cell_type != "code" or not cell.source.strip():
                continue
            client.execute(cell.source, store_history=True, allow_stdin=False)
            reply = client.get_shell_msg(timeout=5)["content"]
            cell.execution_count = reply.get("execution_count")
            while client.iopub_channel.msg_ready():
                message = client.get_iopub_msg(timeout=5)
                if message["msg_type"] == "clear_output":
                    cell.outputs = []
                elif message["msg_type"] in {"stream", "display_data", "execute_result", "error"}:
                    cell.outputs.append(nbformat.v4.output_from_msg(message))
            if reply["status"] != "ok":
                raise RuntimeError(f"Cell {index}: {reply.get('ename')}: {reply.get('evalue')}")
            result["executed_code_cells"] += 1
        # Inspect the result already computed by the notebook; no substitute metrics.
        metrics = manager.kernel.shell.user_ns["LAB_RESULT"]
        result["metrics"] = json.loads(json.dumps(metrics, allow_nan=False))
        assert result["executed_code_cells"] == result["code_cells"]
        result["status"] = "PASS"
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        if client is not None:
            client.stop_channels()
        manager.shutdown_kernel()
        destination = path if in_place and result["status"] == "PASS" else LABS / "executed" / path.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        nbformat.validate(notebook)
        nbformat.write(notebook, destination)
        result["executed_notebook"] = str(destination.relative_to(LABS))
        result["executed_file_sha256"] = hashlib.sha256(destination.read_bytes()).hexdigest()
        result["duration_seconds"] = round(time.monotonic() - started, 3)
        result["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
        result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_inprocess(path, in_place, timeout, temp):
    result_path = Path(temp) / "worker-result.json"
    result_path.unlink(missing_ok=True)
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", str(path),
               "--worker-result", str(result_path)]
    if in_place:
        command.append("--in-place")
    # The worker executes cells synchronously; a process deadline bounds the whole notebook.
    try:
        subprocess.run(command, check=True, timeout=timeout)
        return json.loads(result_path.read_text(encoding="utf-8"))
    except (subprocess.SubprocessError, OSError) as exc:
        return {"notebook": path.name, "status": "FAIL", "error": str(exc), "duration_seconds": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebooks", nargs="*", help="Notebook names/stems; defaults to both public demos")
    parser.add_argument("--in-place", action="store_true", help="Save successful outputs in source notebooks")
    parser.add_argument("--timeout", type=int, default=600, help="Seconds per notebook worker process")
    parser.add_argument("--worker", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--worker-result", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--report", type=Path, default=LABS / "validation" / "latest.json")
    args = parser.parse_args()
    if args.worker:
        if args.worker_result is None:
            parser.error("--worker-result is required with --worker")
        inprocess_worker(args.worker.resolve(), args.worker_result.resolve(), args.in_place)
        return 0
    requested = set(args.notebooks)
    paths = [path for path in sorted(NOTEBOOKS.glob("*.ipynb"))
             if not requested or path.name in requested or path.stem in requested]
    matched = {name for name in requested if any(name in (p.name, p.stem) for p in paths)}
    if not paths or matched != requested:
        parser.error(f"Unknown notebook(s): {sorted(requested - matched)}")

    settings = {
        "PYTHONHASHSEED": "42", "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2",
        "MKL_NUM_THREADS": "2", "TF_NUM_INTRAOP_THREADS": "2", "TF_NUM_INTEROP_THREADS": "2",
        "TF_ENABLE_ONEDNN_OPTS": "0", "TF_CPP_MIN_LOG_LEVEL": "2", "PYDEVD_DISABLE_FILE_VALIDATION": "1",
    }
    os.environ.update(settings)
    report = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "platform": platform.platform(),
        "packages": package_versions(), "execution_settings": settings,
        "mode": "full_data", "fresh_kernel_per_notebook": True, "fresh_process_per_notebook": True,
        "backend": "ipykernel.inprocess", "kernel_transport": "inprocess-no-sockets", "notebooks": [],
    }
    with tempfile.TemporaryDirectory(prefix="plan01-kernel-") as temp:
        for i, path in enumerate(paths, start=1):
            print(f"[{i}/{len(paths)}] {path.name}", flush=True)
            result = run_inprocess(path, args.in_place, args.timeout, temp)
            report["notebooks"].append(result)
            print(f"  {result['status']} ({result['duration_seconds']} s)", flush=True)
            if result["status"] == "FAIL":
                print(result["error"], file=sys.stderr, flush=True)
    report["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    report["passed"] = sum(row["status"] == "PASS" for row in report["notebooks"])
    report["total"] = len(paths)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Result: {report['passed']}/{report['total']} | {args.report}", flush=True)
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
