import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")

# Daten für die Services
data = {
    "Service": [
        "E-Commerce-Plattform-Service",
        "Mitarbeiterarbeitsplatz-Service",
        "Kommunikationsplattform-Service",
        "Kundendatenmanagement-Service",
        "Finanzbuchhaltungs-Service"
    ],
    "Kritikalität": [3, 3, 3, 2, 1],  # 1 = niedrig, 3 = hoch
    "SLA-Verletzungen": [3, 1, 2, 2, 1],  # 1 = gering, 3 = hoch
    "Priorität": ["Hoch", "Gering", "Mittel", "Mittel", "Gering"]
}

# Erstellen eines DataFrames
df = pd.DataFrame(data)

# Farbschema für die Prioritäten
palette = {
    "E-Commerce-Plattform-Service": "red",
    "Mitarbeiterarbeitsplatz-Service": "orange",
    "Kommunikationsplattform-Service": "green",
    "Kundendatenmanagement-Service": "blue",
    "Finanzbuchhaltungs-Service": "purple",
}

# Plot erstellen
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="SLA-Verletzungen",
    y="Kritikalität",
    hue="Service",
    palette=palette,
    size="Priorität",
    sizes=(100, 300),
    legend="auto"
)

# Plot-Anpassungen
plt.title("Portfolioanalyse der Business-IT-Services", fontsize=16)
plt.xlabel("Anzahl der SLA-Verletzungen", fontsize=12)
plt.ylabel("Kritikalität", fontsize=12)
plt.xticks([1, 2, 3], ["Gering", "Mittel", "Hoch"])
plt.yticks([1, 2, 3], ["Niedrig", "Mittel", "Hoch"])
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Priorität", title_fontsize=12,
           fontsize=10, loc="lower right")

# Anzeigen des Plots
plt.tight_layout()
plt.savefig("portfolioanalyse.png")
plt.close()
