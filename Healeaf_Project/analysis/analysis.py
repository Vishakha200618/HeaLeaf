import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/healeaf_dataset.csv")

# -----------------------------
# Average Stress Level
# -----------------------------
average_stress = df["Stress_Level"].mean()

print("\nAverage Stress Level:", average_stress)

# -----------------------------
# Mood Distribution Pie Chart
# -----------------------------
mood_counts = df["Mood"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    mood_counts,
    labels=mood_counts.index,
    autopct='%1.1f%%'
)

plt.title("Mood Distribution")

plt.show()

# -----------------------------
# Sleep Hours vs Stress Level
# -----------------------------
plt.figure(figsize=(8,5))

plt.scatter(
    df["Sleep_Hours"],
    df["Stress_Level"]
)

plt.xlabel("Sleep Hours")
plt.ylabel("Stress Level")
plt.title("Sleep Hours vs Stress Level")

plt.show()

# -----------------------------
# Academic Pressure Distribution
# -----------------------------
pressure_counts = df["Academic_Pressure"].value_counts()

plt.figure(figsize=(6,4))

plt.bar(
    pressure_counts.index,
    pressure_counts.values
)

plt.xlabel("Academic Pressure")
plt.ylabel("Number of Students")
plt.title("Academic Pressure Distribution")

plt.show()