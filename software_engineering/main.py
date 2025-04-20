# Creates a bar chart displaying the average resolution time (MTTR), ticket count, first call resolution rate, and escalated incidents
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

OUTPUT_FILE = "outputs.png"

sns.set_theme(style="darkgrid")

# Simulated data for ticket creation, resolution times, first call resolution rate, and escalated incidents
data = {
    "Monat": [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ],
    "Anzahl_Tickets": [180, 140, 200, 160, 180, 190, 120, 130, 150, 170, 200, 230],
    # Simulated MTTR in hours
    "MTTR": [5.2, 4.8, 6.0, 5.5, 5.0, 4.9, 6.5, 6.8, 5.7, 5.3, 4.6, 4.2],
    # Simulated First Call Resolution Rate in percentage
    "First_Call_Resolution_Rate": [85, 87, 83, 86, 88, 89, 82, 80, 84, 86, 90, 91],
    # Simulated number of escalated incidents
    "Eskalierte_Incidents": [20, 15, 25, 18, 22, 20, 30, 35, 28, 25, 18, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot for Anzahl_Tickets
sns.barplot(
    data=df,
    x="Monat",
    y="Anzahl_Tickets",
    palette="Blues_d",
    ax=ax1
)
ax1.set_ylabel("Anzahl Tickets", fontsize=12, color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Line plot for MTTR
ax2 = ax1.twinx()
sns.lineplot(
    data=df,
    x="Monat",
    y="MTTR",
    color="red",
    marker="o",
    label="MTTR (Stunden)",
    ax=ax2
)

# Line plot for First Call Resolution Rate
sns.lineplot(
    data=df,
    x="Monat",
    y="First_Call_Resolution_Rate",
    color="green",
    marker="s",
    label="First Call Resolution Rate (%)",
    ax=ax2
)

# Line plot for escalated incidents
sns.lineplot(
    data=df,
    x="Monat",
    y="Eskalierte_Incidents",
    color="purple",
    marker="d",
    label="Eskalierte Incidents",
    ax=ax2
)

ax2.set_ylabel(
    "MTTR (Stunden) / First Call Resolution Rate (%) / Eskalierte Incidents", fontsize=12)
ax2.tick_params(axis="y")

# Plot adjustments
plt.title("Anzahl Tickets, MTTR, Erstlösungsquote und Eskalierte Incidents pro Monat", fontsize=16)
ax1.set_xlabel("Monat", fontsize=12)
ax1.set_xticklabels(df["Monat"], rotation=45)
ax1.grid(True, linestyle="--", alpha=0.6)

# Add legend
ax1.legend(["Anzahl Tickets"], loc="upper left")
ax2.legend(loc="upper right")

plt.tight_layout()

# Save the plot
plt.savefig(OUTPUT_FILE, dpi=300)
plt.close()
