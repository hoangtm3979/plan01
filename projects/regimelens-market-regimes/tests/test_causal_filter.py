from pathlib import Path
import sys, unittest
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from chronological_experiment import causal_filter

class FixedModel:
    startprob_=np.array([.5,.5])
    transmat_=np.array([[.8,.2],[.2,.8]])
    means_=np.array([[-1.],[1.]])
    covars_=np.array([[[1.]],[[1.]]])

class ForwardFiltering(unittest.TestCase):
    def test_first_observation_matches_hand_calculation(self):
        p=causal_filter(FixedModel(),np.array([[1.]]))[0]
        self.assertTrue(np.allclose(p,[1/(1+np.exp(2)),1/(1+np.exp(-2))]))
    def test_future_does_not_change_previous_probabilities(self):
        x=np.array([[-1.],[0.],[1.]])
        self.assertTrue(np.allclose(causal_filter(FixedModel(),x)[:2],causal_filter(FixedModel(),np.vstack([x[:2],[[100.]]]))[:2]))
    def test_probabilities_are_finite_normalized(self):
        p=causal_filter(FixedModel(),np.array([[-1.],[0.],[100.]]))
        self.assertTrue(np.isfinite(p).all());self.assertTrue(np.allclose(p.sum(axis=1),1))

if __name__=='__main__':unittest.main()
