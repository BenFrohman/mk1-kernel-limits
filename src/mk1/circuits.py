# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Benjamin Stanley Frohman
"""Qiskit compute-uncompute circuits for the corrected MK-1 ("zz") map."""
from __future__ import annotations

import numpy as np
from qiskit import QuantumCircuit


def points(seed: int = 7, m: int = 4) -> np.ndarray:
    return np.random.default_rng(seed).normal(size=(m, 2))


def feature_circuit(x) -> QuantumCircuit:
    x0, x1 = float(x[0]), float(x[1])
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    qc.rz(2 * x0, 0)
    qc.rz(2 * x1, 1)
    qc.cx(0, 1)
    qc.rz(2 * x0 * x1, 1)  # phase on the TARGET: entangling exp(-i x0 x1 Z⊗Z)
    qc.cx(0, 1)
    return qc


def kernel_circuit(x, xp, measure: bool = True) -> QuantumCircuit:
    qc = feature_circuit(x).compose(feature_circuit(xp).inverse())
    if measure:
        qc.measure_all()
    return qc


def pairs(m: int):
    return [(i, j) for i in range(m) for j in range(i + 1, m)]
