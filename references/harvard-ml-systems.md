# Harvard CS249r / MLSysBook — Introduction to Machine Learning Systems

**Author:** Vijay Janapa Reddi (Harvard University)  
**Textbook:** *Introduction to Machine Learning Systems* (MIT Press, 2026)  
**Open-access book website:** https://mlsysbook.ai/  
**Official source repository:** https://github.com/harvard-edge/cs249r_book  
**Publisher:** https://mitpress.mit.edu/9780262058889/introduction-to-machine-learning-systems/  
**Scope:** Machine Learning Systems Engineering (broader than MLOps alone)

The MIT Press hardcover listing describes **1,032 pages**. Page counts may vary by edition and format.

## What it covers

The book develops a first-principles view of the complete ML systems lifecycle. Its main progression includes **Foundations, Build, Optimize, and Deploy**, with attention to:

- Data engineering, data quality, and the ML workflow.
- Neural network computation, model architectures, and framework internals.
- Training systems, compute/memory constraints, and model optimization.
- Inference, serving, benchmarking, performance, and cost trade-offs.
- MLOps, production reliability, security, privacy, fairness, and sustainability.

The official MLSysBook project also hosts related material, labs, and tools. Some additional volumes are previews or works in progress; consult the original project for their current status.

## Selective reading for applied AI engineering

| Priority | Study area | Evidence-oriented exercise |
| --- | --- | --- |
| P0 | Data pipelines, dataset quality, and evaluation | Trace data-to-model provenance and prevent leakage |
| P0 | Serving, latency, throughput, and reliability | Design a small benchmark and explain the bottleneck |
| P0 | ML operations and monitoring | Specify versioning, observability, and failure response |
| P1 | Training and optimization | Compare alternatives with explicit resource constraints |
| P1 | Security, governance, and responsible deployment | Define boundaries, failure cases, and review evidence |
| P2 | Detailed hardware internals or distributed scaling | Study when an actual system requirement makes them relevant |

## Personal practice ideas (planned, not completed)

- Create a traceable dataset → features → model → evaluation map for an existing project.
- Explain a production ML failure in terms of system boundaries, rather than model accuracy alone.
- Document a reproducibility or monitoring checklist linked to a test or demo.

## Licensing and attribution

The **MLSysBook textbook materials** are published under **CC BY-NC-SA 4.0**; other components of the upstream repository use their own licenses. Consult the authoritative upstream license before copying or adapting any content.

This repository contains **my links and original reading notes only**. It does not redistribute the full textbook, imply affiliation with Harvard, or claim that I completed CS249r.

_Last reviewed: October 2026._
