
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

degree_folder = base_path / "output" / "project_output_final" / "degrees"
output_folder = base_path / "visualization"

csv_file = next(degree_folder.glob("part-*.csv"))

df = pd.read_csv(csv_file)

print("Total users:", len(df))
print("\nDegree statistics:")
print(df["totalDegree"].describe())

plt.figure(figsize=(10, 6))

plt.hist(df["totalDegree"], bins=30, edgecolor="black")

plt.title("Degree Distribution of College Messaging Network")
plt.xlabel("Total Degree")
plt.ylabel("Number of Users")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

output_file = output_folder / "degree_distribution.png"
plt.savefig(output_file, dpi=300)
plt.show()

print("\nVisualization saved at:", output_file)

