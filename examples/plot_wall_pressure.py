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
