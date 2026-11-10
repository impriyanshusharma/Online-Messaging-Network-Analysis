
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

degree_folder = base_path / "output" / "project_output_final" / "degrees"
output_folder = base_path / "visualization"

csv_file = next(degree_folder.glob("part-*.csv"))
df = pd.read_csv(csv_file)

top10 = df.nlargest(10, "totalDegree").sort_values("totalDegree")

plt.figure(figsize=(10, 6))

plt.barh(top10["userId"].astype(str), top10["totalDegree"])

plt.title("Top 10 Users by Total Degree")
plt.xlabel("Total Degree")
plt.ylabel("User ID")
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

output_file = output_folder / "top_degree_users.png"
plt.savefig(output_file, dpi=300)
plt.show()

print(top10.to_string(index=False))
print("\nSaved:", output_file)

