
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

degree_folder = base_path / "output" / "project_output_final" / "degrees"
output_folder = base_path / "visualization"

csv_file = next(degree_folder.glob("part-*.csv"))
df = pd.read_csv(csv_file)

plt.figure(figsize=(10, 6))

plt.hist(df["totalDegree"], bins=30, edgecolor="black")

plt.yscale("log")
plt.title("Log-Scale Degree Distribution of College Messaging Network")
plt.xlabel("Total Degree")
plt.ylabel("Number of Users (Log Scale)")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

output_file = output_folder / "degree_distribution_log.png"
plt.savefig(output_file, dpi=300)
plt.show()

print("Saved:", output_file)

