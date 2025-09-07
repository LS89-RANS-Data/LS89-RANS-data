
---

##  Notes

- Averages are computed across three turbulence models:
- `k-omega-SST`
- `k-epsilon realizable`
- `k-omega-SST-gamma`

- **Data files** generally contain:
- **Normalized coordinates**: (`y/t`, `s/c`)
- **Quantities of interest** (as listed above)
- Both **mean** and **standard deviation** across turbulence models

---

##  Usage & Recommendations

1. **Navigating the data**  
 - For adiabatic cases: explore under `Adiabatic/[quantity]_mean` directories.  
 - For diabatic cases: navigate via `Diabatic/T_rat_[value]/[quantity]_mean`.

2. **Reading the files**  
 - Files are often tab-delimited or whitespace-separated.  
 - Typical columns include: normalized coordinates, mean values, standard deviations—check the first few rows or header for specifics.

3. **Further processing**  
 - Use scripting tools (e.g., Python with `numpy` or `pandas`) to parse and visualize the data.  
 - Help future users by including a small example script or Jupyter notebook (optional).

---

##  Potential Enhancements (Optional)

- **README Extension**: Add a table summarizing contents, example files, or folder structure.
- **Documentation Folder**: Consider adding a `docs/` directory explaining how data was generated or validated.
- **Example Visualizations**: Include plots of wall pressure or Mach number distributions to illustrate typical outputs.
- **Usage Notebook**: Provide a Jupyter notebook demonstrating how to read data, compare models, or visualize results.

---

##  Summary

- **Project purpose**: RANS data for LS89 turbine blade (adiabatic + diabatic).
- **Organization**:
- `Adiabatic/`: grouped by quantity, MUR cases, turbulence models.
- `Diabatic/`: first grouped by temperature ratio, then following adiabatic structure.
- **Contents**: normalized coordinates, mean and standard deviation for each quantity.
- **Suggestions**: Improve ease of use with examples, summaries, and visual aids.

---

**Let me know** if you'd like help generating an example visualization (e.g., using Python) or drafting a sample Jupyter notebook to accompany the README!
::contentReference[oaicite:0]{index=0}

