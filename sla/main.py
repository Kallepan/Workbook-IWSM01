import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")

# Daten für die Services
services = ["CRM-System", "ERP-System", "E-Commerce-Plattform",
            "Intranet-Kommunikationsplattform", "IT-Support-Service"]
kritikalitaet = [4, 5, 5, 3, 4]
sla_verletzungen = [2, 3, 4, 1, 5]

data = pd.DataFrame({
    "Service": services,
    "Kritikalität": kritikalitaet,
    "SLA-Verletzungen": sla_verletzungen
})

# Farbschema für die Services
palette = {
    "CRM-System": "red",
    "ERP-System": "orange",
    "E-Commerce-Plattform": "green",
    "Intranet-Kommunikationsplattform": "blue",
    "IT-Support-Service": "purple",
}

# Diagramm erstellen
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=data, x="SLA-Verletzungen", y="Kritikalität", hue="Service",
    s=100, palette=palette)

# Punkte beschriften
for i in range(data.shape[0]):
    scatter_plot.text(data['SLA-Verletzungen'][i] + 0.1,
                      data['Kritikalität'][i] - 0.1,
                      data['Service'][i], fontsize=9)

# Achsenbeschriftung und Titel
plt.title("Portfolioanalyse: Kritikalität vs. Anzahl SLA-Verletzungen", fontsize=14)
plt.xlabel("Anzahl SLA-Verletzungen", fontsize=12)
plt.ylabel("Kritikalität", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(range(1, 6))
plt.yticks(range(1, 6))

plt.tight_layout()
plt.savefig("sla.png")
plt.close()
