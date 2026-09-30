import numpy as np

from pathlib import Path

from typing import List, Tuple


def get_edges(edgelist_path: Path) -> List[Tuple[int]]:
    with open(edgelist_path, "r") as f:
        text = f.read()

    edges = []
    for edge in text.split():
        nodes = edge.split(",")
        edges.append((int(nodes[0]), int(nodes[1])))

    return edges

def sample_negative_pairs(
    known_edges: np.ndarray,
    node_ids: np.ndarray,
    n_pairs: int,
    seed: int = 42,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    known = {(min(u, v), max(u, v)) for u, v in known_edges}
    negatives = set()
    while len(negatives) < n_pairs:
        node_u, node_v = rng.choice(node_ids, size=2, replace=False)
        pair = (min(node_u, node_v), max(node_u, node_v))
        if pair not in known:
            negatives.add(pair)
    return np.array(sorted(negatives))