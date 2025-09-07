# LS89-RANS-Data 🌀

RANS (Reynolds-Averaged Navier–Stokes) simulation dataset for the **LS89 turbine blade**, under both **adiabatic** and **diabatic** wall conditions. Includes outputs from multiple turbulence models for comparative analyses and validation.

---

## Table of Contents
- [Repository Structure](#repository-structure)
  - [Adiabatic Conditions](#adiabatic-conditions)
  - [Diabatic Conditions](#diabatic-conditions)
- [Data Description](#data-description)
- [Usage Examples](#usage-examples)
  - [Plotting Scripts](#plotting-scripts)
- [Contributing](#contributing)
- [License](#license)
- [Corresponding Author](#corresponding-author)
- [Credits](#credits)

---

## Repository Structure

Organized by thermal condition, then by physical quantity and simulation parameters.

### Adiabatic Conditions (`Adiabatic/`)

Each quantity (e.g., `Mach_is`, `Wall_pressure`, `Turbulent_kinetic_energy`) has its own folder. Inside each, you'll find files named by turbulence model and MUR case:

```

Adiabatic/Mach\_is/
├── K-epsilon\_MUR43\_M\_is.txt
├── K-epsilon\_MUR45\_M\_is.txt
├── K-epsilon\_MUR47\_M\_is.txt
├── K-omega-SST\_MUR43\_M\_is.txt
├── K-omega-SST\_MUR45\_M\_is.txt
├── K-omega-SST\_MUR47\_M\_is.txt
├── K-omega-SST-intermittency\_MUR43\_M\_is.txt
├── K-omega-SST-intermittency\_MUR45\_M\_is.txt
└── K-omega-SST-intermittency\_MUR47\_M\_is.txt

```

### Diabatic Conditions (`Diabatic/`)

First grouped by wall-to-recovery **temperature ratio** (`T_rat_0.5` … `T_rat_1.0`), then by quantity, each following the same model/MUR naming:

```

Diabatic/T\_rat\_0.6/Wall\_pressure\_mean/
├── K-epsilon\_MUR43\_P\_wall\_mean\_std.txt
├── K-epsilon\_MUR45\_P\_wall\_mean\_std.txt
├── K-epsilon\_MUR47\_P\_wall\_mean\_std.txt
├── K-omega-SST\_MUR43\_P\_wall\_mean\_std.txt
├── K-omega-SST\_MUR45\_P\_wall\_mean\_std.txt
├── K-omega-SST\_MUR47\_P\_wall\_mean\_std.txt
├── K-omega-SST-intermittency\_MUR43\_P\_wall\_mean\_std.txt
├── K-omega-SST-intermittency\_MUR45\_P\_wall\_mean\_std.txt
└── K-omega-SST-intermittency\_MUR47\_P\_wall\_mean\_std.txt

````

**Highlights:**
- Top-level: `Adiabatic/` vs. `Diabatic/`.
- Structure mirrors across conditions with consistent naming for turbulence models and MUR cases.

---

## Data Description

- **Turbulence models included:**
  - `k-epsilon`
  - `k-omega-SST`
  - `k-omega-SST-intermittency`
- Filenames reflect MUR cases (43, 45, 47) and indicate whether they include mean and standard deviation (e.g., `_mean_std`).
- Files are whitespace-delimited `.txt` and typically contain:
  - Normalized coordinates (`s/c`, `y/t`, etc.)
  - Quantity values (e.g., Mach isentropic, wall pressure coefficient)
  - Standard deviations across models (in mean/std files)

---

## Usage Examples

### Plotting Scripts

Scripts available in the `examples/` folder:

#### 1. Adiabatic Wall Pressure (`examples/plot_wall_pressure.py`)

```python
import pandas as pd
import matplotlib.pyplot as plt

files = {
    "k-epsilon (MUR43)": "Adiabatic/Wall_pressure_mean/K-epsilon_MUR43_P_wall_mean_std.txt",
    "k-omega-SST (MUR43)": "Adiabatic/Wall_pressure_mean/K-omega-SST_MUR43_P_wall_mean_std.txt",
    "k-omega-SST-int. (MUR43)": "Adiabatic/Wall_pressure_mean/K-omega-SST-intermittency_MUR43_P_wall_mean_std.txt",
}
plt.figure(figsize=(8,6))
for label, fname in files.items():
    df = pd.read_csv(fname, delim_whitespace=True, header=None,
                     names=["s/c", "Cp_mean", "Cp_std"])
    plt.errorbar(df["s/c"], df["Cp_mean"], yerr=df["Cp_std"],
                 fmt="-o", capsize=3, label=label)
plt.xlabel("s/c (normalized)")
plt.ylabel("Wall Pressure Coefficient")
plt.title("LS89 Adiabatic – Wall Pressure Distribution")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
````

#### 2. Diabatic Comparison (`examples/plot_trat_comparison.py`)

```python
import pandas as pd
import matplotlib.pyplot as plt

base = "Diabatic/T_rat_{}/Wall_pressure_mean/K-epsilon_MUR45_P_wall_mean_std.txt"
t_rat_values = ["0.5", "0.7", "1.0"]
plt.figure(figsize=(8,6))
for T in t_rat_values:
    df = pd.read_csv(base.format(T), delim_whitespace=True, header=None,
                     names=["s/c", "Cp_mean", "Cp_std"])
    plt.errorbar(df["s/c"], df["Cp_mean"], yerr=df["Cp_std"],
                 fmt="-o", capsize=3, label=f"T_rat = {T}")
plt.xlabel("s/c (normalized)")
plt.ylabel("Wall Pressure Coefficient")
plt.title("LS89 Diabatic – Wall Pressure vs T_rat")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
```

**Run with:**

```bash
python examples/plot_wall_pressure.py
python examples/plot_trat_comparison.py
```

---

## Contributing

We welcome your contributions! Please:

1. **Fork** the repository and create a new branch (`feature/your-change`).
2. **Commit** changes with meaningful messages.
3. **Push** your branch to GitHub.
4. **Open a Pull Request** with a clear description of your change.

Please maintain consistency in formatting and documentation.

---

## License

This dataset is released under the **BSD 3-Clause License (for datasets)**. See the [`LICENSE`](./LICENSE) file for details.

---

## Corresponding Author

For inquiries or collaboration, contact:

**Francesco De Vanna** — [francesco.devanna@unipd.it](mailto:francesco.devanna@unipd.it)

---

## Credits

Maintained by the **LS89-RANS-Data** contributors. If you use this dataset, please also consult our [`CITATION.cff`](./CITATION.cff) for proper citation.

---

**Happy exploring and analyzing!**

```



