# Data Structure of the Repository

This repository contains CFD simulation data for the study of a turbine blade, organized into two main folders:

## 📂 1. Adiabatic
Contains results from **RANS simulations** with **adiabatic wall conditions** of the blade.

### Internal structure
- Data is divided by **turbulence model** and **MUR case**:
  - **MUR 43, 45, 47** → high-subsonic and transonic cases.
  - **Turbulence models**:
    - `k-omega-SST`
    - `k-epsilon realizable`
    - `k-omega-SST-gamma`
- For each MUR, in addition to the individual model data, files with **averages across turbulence models** are also included.

---

## 📂 2. Diabatic
Contains results from **RANS simulations** with **diabatic wall conditions** of the blade.

### Internal structure
- Subfolders for each **T_rat value**:
  - `T_rat_0.5`
  - `T_rat_0.6`
  - `T_rat_0.7`
  - `T_rat_0.8`
  - `T_rat_0.9`
  - `T_rat_1.0`
- Each folder contains the **averaged data** for the MUR cases (43, 45, 47).

---

## 📝 Notes
- Averages are computed across the turbulence models `k-omega-SST`, `k-epsilon realizable`, and `k-omega-SST-gamma`.
- Typical files include:
  - Normalized coordinates (`y/t`,`s/c`)
  - Quantities of interest (e.g., normalized total pressure)
  - Mean and standard deviation across turbulence models
