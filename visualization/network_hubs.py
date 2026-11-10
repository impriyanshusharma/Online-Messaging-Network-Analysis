
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

degree_folder = base_path / "output" / "project_output_final" / "degrees"
edge_folder = base_path / "output" / "project_output_final" / "network_edges"
output_folder = base_path / "visualization"

degree_file = next(degree_folder.glob("part-*.csv"))
edge_file = next(edge_folder.glob("part-*.csv"))

degrees = pd.read_csv(degree_file)
edges = pd.read_csv(edge_file)

top_hubs = degrees.nlargest(5, "totalDegree")
hub_ids = set(top_hubs["userId"])

selected_edges = edges[
    edges["source"].isin(hub_ids) |
    edges["target"].isin(hub_ids)
]

G = nx.DiGraph()
G.add_edges_from(zip(selected_edges["source"], selected_edges["target"]))

degree_map = degrees.set_index("userId")["totalDegree"].to_dict()

positions = nx.spring_layout(G, seed=42, k=0.35, iterations=80)

hub_nodes = [node for node in G.nodes() if node in hub_ids]
other_nodes = [node for node in G.nodes() if node not in hub_ids]

node_sizes = [
    max(20, min(450, degree_map.get(node, 1) * 1.2))
    for node in G.nodes()
]

plt.figure(figsize=(15, 11))

nx.draw_networkx_edges(
    G,
    positions,
    alpha=0.25,
    arrows=True,
    arrowsize=7,
    width=0.5
)

nx.draw_networkx_nodes(
    G,
    positions,
    nodelist=other_nodes,
    node_size=[max(15, min(250, degree_map.get(node, 1))) for node in other_nodes],
    node_color="lightblue",
    alpha=0.7
)

nx.draw_networkx_nodes(
    G,
    positions,
    nodelist=hub_nodes,
    node_size=[max(100, degree_map.get(node, 1) * 1.2) for node in hub_nodes],
    node_color="red",
    alpha=0.9
)

nx.draw_networkx_labels(
    G,
    positions,
    labels={node: str(node) for node in hub_nodes},
    font_size=11,
    font_weight="bold"
)

plt.title("Communication Network Around Top 5 Hubs")
plt.axis("off")
plt.tight_layout()

output_file = output_folder / "network_hubs.png"
plt.savefig(output_file, dpi=300)
plt.show()

print("Top 5 hubs:")
print(top_hubs[["userId", "totalDegree"]].to_string(index=False))
print("\nNodes displayed:", G.number_of_nodes())
print("Directed edges displayed:", G.number_of_edges())
print("Saved:", output_file)

