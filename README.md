# LS89-RANS-Data 🌀

RANS (Reynolds-Averaged Navier–Stokes) simulation data for the **LS89 turbine blade**, available under both **adiabatic** and **diabatic** wall conditions. Encompasses results from multiple turbulence models to support comparative analysis and validation efforts.

---

##  Table of Contents

- [Repository Structure](#repository-structure)
  - [Adiabatic Conditions](#adiabatic-conditions)
  - [Diabatic Conditions](#diabatic-conditions)
- [Data Description](#data-description)
- [Usage Examples](#usage-examples)
  - [Plotting Scripts](#plotting-scripts)
- [Contributing](#contributing)
- [License](#license)
- [Credits & Contact](#credits--contact)

---

##  Repository Structure

The repository is organized based on wall condition, physical quantity, and simulation parameters.

### Adiabatic Conditions (`Adiabatic/`)

Each quantity—such as `Mach_is`, `Wall_pressure`, `Turbulent_kinetic_energy`—has its own folder, and each folder contains files named per turbulence model and MUR case:

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

Organized first by **temperature ratio** folder (`T_rat_0.5`, `T_rat_0.6`, …), then by quantity, each containing similarly named files:

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

**Key structure highlights:**

- Top-level: `Adiabatic/` vs. `Diabatic/`
- **Adiabatic** → quantity folders → files per model + MUR case
- **Diabatic** → temperature ratio → quantity folders → files per model + MUR case

---

##  Data Description

- Supported turbulence models:  
  - `k-epsilon`  
  - `k-omega-SST`  
  - `k-omega-SST-intermittency`

- Filenames include identifiers for MUR cases (e.g., MUR43, MUR45, MUR47) and denote mean and standard deviation where applicable.

- Each text file is whitespace-delimited and contains columns like:  
  - normalized coordinate (`s/c`, `y/t`, etc.)  
  - statistical quantity (e.g., Mach isentropic, pressure coefficient)  
  - standard deviation across models (in mean/std files)

---

##  Usage Examples

### Plotting Scripts

Example Python scripts are available in the following boxes:

1. **Adiabatic Wall Pressure Plot**

```python
# examples/plot_wall_pressure.py
import pandas as pd
import matplotlib.pyplot as plt

files = {
    "k-epsilon (MUR43)": "Adiabatic/Wall_pressure_mean/K-epsilon_MUR43_P_wall_mean_std.txt",
    "k-omega-SST (MUR43)": "Adiabatic/Wall_pressure_mean/K-omega-SST_MUR43_P_wall_mean_std.txt",
    "k-omega-SST-int. (MUR43)": "Adiabatic/Wall_pressure_mean/K-omega-SST-intermittency_MUR43_P_wall_mean_std.txt",
}

plt.figure(figsize=(8, 6))

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

2. **Diabatic Comparison Across Temperature Ratios**

```python
# examples/plot_trat_comparison.py
import pandas as pd
import matplotlib.pyplot as plt

base = "Diabatic/T_rat_{}/Wall_pressure_mean/K-epsilon_MUR45_P_wall_mean_std.txt"
t_rat_values = ["0.5", "0.7", "1.0"]

plt.figure(figsize=(8, 6))

for T in t_rat_values:
    fname = base.format(T)
    df = pd.read_csv(fname, delim_whitespace=True, header=None,
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

**Run these with:**

```bash
python plot_wall_pressure.py
python plot_trat_comparison.py
```

---

## 🤝 Contributing

Contributions are warmly welcomed! Here’s how you can help:

1. **Fork** the repo and create your feature branch (`git checkout -b feature/my-addition`)
2. **Commit** your changes with clear messages
3. **Push** to your branch (`git push origin feature/my-addition`)
4. **Open a Pull Request**, describing your improvements
5. Make sure to keep any existing **Python scripts**, **plots**, and **README formatting** consistent.

---

## License

This project is released under the **[MIT License](./LICENSE)** — feel free to use, modify, and distribute it under these terms.

---

## Credits & Contact

* Developed and maintained by the LS89-RANS-Data contributors.
* For questions, issues, or feedback, feel free to open an issue or reach out on GitHub.

**Happy exploring and visualizing!**

````
