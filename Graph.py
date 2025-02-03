import matplotlib.pyplot as plt
import numpy as np
from statistics import median, mean


x = np.arange(1, 13)
y = np.random.randint(1, 101, size=len(x))

plt.style.use("seaborn-v0_8-darkgrid")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=6, label="Valeurs aléatoires")

med = median(y)
moy = mean(y)

ax.axhline(med, color='red', linestyle='--', linewidth=1.5, label=f"Médiane: {med}")
ax.axhline(moy, color='green', linestyle='--', linewidth=1.5, label=f"Moyenne: {moy}")

ax.text(12.6, med, f"{med}", verticalalignment="center", color="red", fontsize=10)
ax.text(12.6, moy, f"{moy}", verticalalignment="center", color="green", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"], rotation=45)
ax.set_xlabel("Mois", fontsize=12)
ax.set_ylabel("Valeur", fontsize=12)
ax.set_title("Évolution des valeurs aléatoires sur 12 mois", fontsize=14, fontweight="bold")

ax.legend()

plt.show()
