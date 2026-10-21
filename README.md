# Physics Consulting Toolkit

**Remote quantitative modeling & data analysis**  
Physics-informed ODE/PDE solvers • Statistical inference • Clean Python pipelines

Built for independent consulting from anywhere (including PNG).  
Run everything locally in VS Code + Jupyter. Deliver reproducible notebooks and reports to clients.

---

## Quick Start (VS Code)

1. Unzip this folder.
2. Open the folder in VS Code (`File → Open Folder`).
3. Create / select a Python environment (3.10+ recommended).
4. In the integrated terminal:

```bash
pip install -r requirements.txt
```

5. Open any notebook in `notebooks/` and run cells (VS Code will prompt to install the Jupyter extension if needed).
6. Or open a terminal and launch Jupyter:

```bash
jupyter lab
```

---

## Project Layout

```
physics_consulting/
├── README.md
├── requirements.txt
├── src/
│   ├── solvers.py      # ODE wrappers, heat equation, parameter fitting
│   ├── stats.py        # bootstrap, regression, residual diagnostics
│   ├── viz.py          # consistent publication-quality plots
│   └── models/         # reusable physics models
├── notebooks/
│   ├── 01_ode_examples.ipynb
│   ├── 02_pde_heat.ipynb
│   ├── 03_stats_modeling.ipynb
│   └── client_template.ipynb
├── projects/
│   └── sample_client/  # example engagement folder
└── reports/            # place exported HTML/PDF reports here
```

---

## Core Capabilities

| Module       | What it does                                      | Typical use                          |
|--------------|---------------------------------------------------|--------------------------------------|
| `solvers`    | `solve_ode`, `fit_ode_parameters`, `heat_equation_1d`, Lorenz | Dynamical systems, parameter estimation |
| `stats`      | bootstrap, linear/nonlinear regression, diagnostics | Uncertainty, model assessment        |
| `viz`        | time series, phase portraits, fit + residual plots, heatmaps | Client-ready figures                 |

All functions are documented with docstrings. Import them inside notebooks:

```python
import sys
sys.path.insert(0, "..")          # if running from notebooks/
from src import solvers, stats, viz
```

---

## Demonstration Notebooks

- **01_ode_examples.ipynb** – Damped driven oscillator, numerical vs analytic, parameter recovery from noisy data.
- **02_pde_heat.ipynb** – 1-D heat equation (explicit finite difference), stability, visualization.
- **03_stats_modeling.ipynb** – Linear & nonlinear regression, bootstrap confidence intervals, residual checks.
- **client_template.ipynb** – Structured template for real client work (problem → data/model → analysis → conclusions).

---

## Typical Client Workflow

1. Copy `notebooks/client_template.ipynb` into `projects/<client_name>/`.
2. Load data or define the physics model.
3. Use `solvers` / `stats` / `viz` to analyse.
4. Export the notebook to HTML or PDF (`File → Export` in Jupyter, or `jupyter nbconvert`).
5. Deliver the notebook + exported report + any figures.

---

## Environment Notes

- Tested with Python 3.10–3.12.
- Heavy numerical work stays in NumPy/SciPy (no external solvers required).
- For very stiff systems or advanced PDEs you can later add packages; the current core stays lightweight and reliable.

---

## Next Steps for Your Practice

1. Run all three demo notebooks and confirm they work on your machine.
2. Put the repository on GitHub (public portfolio).
3. Update your LinkedIn / Upwork profile with the capability statement below.
4. Start a real (or mock) client folder under `projects/` and practice the full delivery loop.

**Capability statement (copy-paste ready):**

> Computational physicist offering remote quantitative modeling and data analysis. Strong background in classical physics, calculus, ODEs/PDEs and statistics, implemented in clean, reproducible Python (NumPy/SciPy). Deliverables: dynamical-system simulations, parameter estimation with uncertainty, statistical modeling, and publication-quality visualizations. Available for short-term projects and ongoing consulting.

---

## License & Use

Free to use and modify for your consulting work.  
Attribution appreciated but not required.

Built for independent professionals who want rigorous math + practical code.
