import numpy as np
from mk1.circuits import points, pairs
from mk1.kernel import kernel, kernel_closed_form
from mk1.shots import binomial_study, fit_loglog

def test_closed_form_matches():
    P = points()
    for p in P:
        for q in P:
            assert abs(kernel(p, q) - kernel_closed_form(p, q)) < 1e-12

def test_gram_psd():
    P = points()
    G = np.array([[kernel(p, q) for q in P] for p in P])
    assert np.allclose(G, G.T) and np.linalg.eigvalsh(G).min() > -1e-10

def test_pairs():
    assert len(pairs(4)) == 6

def test_binomial_slope():
    n, rms = binomial_study(points())
    slope = fit_loglog(n, rms)
    slope = slope[0] if isinstance(slope, tuple) else slope
    assert -0.6 < slope < -0.4
