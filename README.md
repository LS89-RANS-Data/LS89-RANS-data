# LS89-RANS-Data 🌀

This repository provides **RANS (Reynolds-Averaged Navier–Stokes) simulation data** for the **LS89 turbine blade** under both **adiabatic** and **diabatic** wall conditions.  
The data includes detailed statistics from multiple turbulence models, enabling comparative analysis, benchmarking, and further research.

---

## 📂 Repository Structure

| Condition   | Organization | Available Quantities |
|-------------|--------------|-----------------------|
| **Adiabatic** 🌡️ | Grouped by **quantity** → turbulence model → MUR cases (MUR43, MUR45, MUR47) | Friction coefficient, Mach number, TKE, total pressure, wall pressure |
| **Diabatic** 🔥 | Grouped by **temperature ratio** (`T_rat_0.5` → `T_rat_1.0`) → then by quantity | Friction coefficient, Heat coefficient, Mach number, TKE, wake quantities, wall pressure |

---
Perfect 👌 thanks for the screenshot! Now it’s clear: each **quantity directory** (like `Adiabatic/Mach_is`) directly contains **flat text files**, named by turbulence model + MUR case. No extra subfolders.

Here’s how I’d improve the README directory description to reflect the real tree:

---

## 📂 Repository Structure

The repository is organized by **thermal condition** → **quantity of interest** → **simulation files**.

### 🔹 Adiabatic Conditions (`Adiabatic/`)

- Each subfolder corresponds to a physical quantity (e.g., `Mach_is`, `Wall_pressure`, `Turbulent_kinetic_energy`).
- Inside each folder, you’ll find **one text file per turbulence model and MUR case**.

📁 Example (`Adiabatic/Mach_is/`):
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

---

### 🔹 Diabatic Conditions (`Diabatic/`)

- First grouped by wall-to-recovery **temperature ratio** (`T_rat_0.5`, `T_rat_0.6`, …, `T_rat_1.0`).
- Inside each `T_rat_*` folder, data is further split by **quantity** (e.g., `Friction_coefficient_mean`, `Wall_pressure_mean`).
- Each quantity folder contains one file per turbulence model and MUR case, following the same naming convention.

📁 Example (`Diabatic/T_rat_0.6/Wall_pressure_mean/`):
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

```

---

✅ **Key points:**
- **Top-level split**: `Adiabatic/` vs. `Diabatic/`
- **Adiabatic** → quantity folders → direct files per turbulence model + MUR case
- **Diabatic** → temperature ratio folders → quantity folders → direct files per turbulence model + MUR case

---

## 📊 Data Details

- **Turbulence models averaged**:
- `k-omega-SST`
- `k-epsilon realizable`
- `k-omega-SST-gamma`

- **File contents**:
- Normalized coordinates (e.g., `y/t`, `s/c`)
- Mean values  
- Standard deviations across turbulence models

---

## ⚙️ Usage Recommendations

1. **Navigation**  
 - Adiabatic cases: check `Adiabatic/[quantity]_mean`  
 - Diabatic cases: check `Diabatic/T_rat_[value]/[quantity]_mean`

2. **Reading data**  
 - Files are whitespace-separated text files.  
 - Columns typically: coordinates → mean → std.  

 ✅ Example (Python + Pandas):  
 ```python
 import pandas as pd

 df = pd.read_csv("Adiabatic/Wall_pressure_mean/MUR43_P_wall_mean_std.txt",
                  delim_whitespace=True, header=None,
                  names=["s/c", "Pressure_mean", "Pressure_std"])

 print(df.head())
````

3. **Visualization**
   You can easily plot distributions (e.g., pressure coefficient, Mach profiles) with `matplotlib`.

---

### 📊 Example 1: Plot Wall Pressure (Adiabatic case)

```python
#!/usr/bin/env python3
"""
Plot wall pressure coefficient for LS89 - Adiabatic case
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load one or more datasets (Adiabatic / Wall_pressure_mean)
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
plt.title("LS89 Adiabatic - Wall Pressure Distribution")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
```

---

### 📊 Example 2: Compare Temperature Ratios (Diabatic case)

```python
#!/usr/bin/env python3
"""
Compare wall pressure for different T_rat in Diabatic cases
"""

import pandas as pd
import matplotlib.pyplot as plt

# Example: wall pressure at MUR45, different T_rat values
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
plt.title("LS89 Diabatic - Wall Pressure vs T_rat")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
```

---



## ✨ Summary

This repository provides a **comprehensive RANS dataset** for the LS89 turbine blade under adiabatic and diabatic conditions.
It is structured for easy access, with normalized coordinates, mean values, and standard deviations across turbulence models.

🔍 Researchers can use it for **model validation, comparative studies, and uncertainty quantification**.

---

💡 *Contributions, feedback, or derived visualizations are welcome — feel free to open an issue or PR!*

```

---

👉 Do you want me to also prepare a **ready-to-use Jupyter notebook** (`examples/plot_wall_pressure.ipynb`) so users can directly run and visualize the data after cloning the repo?
```

