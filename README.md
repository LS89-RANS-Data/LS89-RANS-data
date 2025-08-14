# Data Structure of the Repository

This repository contains **RANS simulation data** for a turbine blade, for both **adiabatic** and **diabatic wall conditions**.

---

## 📂 1. Adiabatic
Contains results for **adiabatic wall conditions**.

### Structure
- The top-level folders correspond to the **quantities of interest**, which can be **averaged** or **individual**.  
- The quantities available in this repository are:
  - `Friction_coefficient_mean`
  - `Mach_is_mean`
  - `Turbulent_kinetic_energy`
  - `Wake_density`
  - `Wake_temperature`
  - `Wake_total_pressure`
  - `Wall_pressure_mean`
- Inside each quantity folder:
  - Data is organized by **turbulence model** and **MUR case** (43, 45, 47 → high-subsonic and transonic).
- Files typically contain **mean values** and **standard deviations** across turbulence models.

### Example file path

Adiabatic\Wall_pressure_mean\MUR43_P_wall_mean_std.txt

---

## 📂 2. Diabatic
Contains results for **diabatic wall conditions**.

### Structure
- First, select the **T_rat value** (0.5 → 1.0):
  - `T_rat_0.5`, `T_rat_0.6`, …, `T_rat_1.0`
- Inside each `T_rat` folder, the structure mirrors the adiabatic case:
  - Top-level folders for the **quantities of interest** (averaged or individual, same list as above)
  - Inside each quantity folder: **turbulence model** and **MUR case**.

### Example file path

Diabatic\T_rat_0.6\Friction_coefficient_mean\MUR47_cf_mean_std.txt

---

## 📝 Notes
- Averages are computed across turbulence models: `k-omega-SST`, `k-epsilon realizable`, `k-omega-SST-gamma`.
- Typical files contain:
  - Normalized coordinates (`y/t`, `s/c`)
  - Quantities of interest (as listed above)
  - Mean and standard deviation across turbulence models

