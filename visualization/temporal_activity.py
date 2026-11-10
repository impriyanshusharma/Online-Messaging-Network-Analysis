
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

output_root = base_path / "output" / "project_output_final"
visualization_folder = base_path / "visualization"

daily_file = next((output_root / "daily").glob("part-*.csv"))
monthly_file = next((output_root / "monthly").glob("part-*.csv"))

daily = pd.read_csv(daily_file)
monthly = pd.read_csv(monthly_file)

daily["date"] = pd.to_datetime(daily["date"])
monthly["month"] = pd.to_datetime(monthly["month"])

daily = daily.sort_values("date")
monthly = monthly.sort_values("month")

plt.figure(figsize=(13, 6))

plt.plot(daily["date"], daily["messageCount"], linewidth=1.5)

plt.title("Daily Messaging Activity - CollegeMsg Network")
plt.xlabel("Date")
plt.ylabel("Number of Messages")
plt.grid(alpha=0.3)
plt.xticks(rotation=45)

plt.tight_layout()

daily_output = visualization_folder / "daily_messaging_activity.png"
plt.savefig(daily_output, dpi=300)
plt.show()

plt.figure(figsize=(10, 6))

plt.bar(monthly["month"].dt.strftime("%b %Y"), monthly["messageCount"])

plt.title("Monthly Messaging Activity - CollegeMsg Network")
plt.xlabel("Month")
plt.ylabel("Number of Messages")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

monthly_output = visualization_folder / "monthly_messaging_activity.png"
plt.savefig(monthly_output, dpi=300)
plt.show()

print("Busiest day:")
print(daily.loc[daily["messageCount"].idxmax()].to_string())

print("\nBusiest month:")
print(monthly.loc[monthly["messageCount"].idxmax()].to_string())

print("\nTotal daily messages:", daily["messageCount"].sum())
print("Total monthly messages:", monthly["messageCount"].sum())

print("\nSaved:", daily_output)
print("Saved:", monthly_output)

