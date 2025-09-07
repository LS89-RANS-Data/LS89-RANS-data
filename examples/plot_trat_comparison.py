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

