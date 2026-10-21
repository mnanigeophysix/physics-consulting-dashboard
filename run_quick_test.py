#!/usr/bin/env python
"""
Quick smoke test – run this after installing requirements to verify the toolkit works.
"""

import sys
sys.path.insert(0, ".")

import numpy as np
from src import solvers, stats, viz

print("=== Physics Consulting Toolkit – Quick Test ===\n")

# ODE
t_eval = np.linspace(0, 10, 200)
sol = solvers.solve_ode(
    solvers.harmonic_oscillator,
    (0, 10),
    y0=[1.0, 0.0],
    t_eval=t_eval,
    args=(2.0, 0.2, 0.0, 0.0),
)
assert sol.success, "ODE solver failed"
print("✓ ODE solver (damped oscillator)")

# Heat equation
x = np.linspace(0, 1, 21)
u0 = np.sin(np.pi * x)
u = solvers.heat_equation_1d(u0, dx=x[1]-x[0], dt=0.001, n_steps=50, alpha=0.1)
assert u.shape == (51, 21)
print("✓ Heat equation solver")

# Stats
x = np.linspace(0, 5, 30)
y = 2 * x + 1 + 0.3 * np.random.randn(30)
res = stats.linear_regression(x, y)
assert "slope" in res and res["r_squared"] > 0.8
print("✓ Linear regression")

boot = stats.bootstrap(np.random.randn(50), n_boot=500)
assert "ci_low" in boot
print("✓ Bootstrap")

print("\nAll core tests passed. You are ready to open the notebooks.")
