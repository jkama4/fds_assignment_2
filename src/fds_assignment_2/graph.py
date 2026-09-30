import pandas as pd
import numpy as np
import networkx as nx

from typing import Dict, Tuple, Set

class LinkPredictionGraph(nx.Graph):

    def __init__(self, node_ids: np.ndarray, edges: np.ndarray, attributes: pd.DataFrame):
        super().__init__()
        self.add_nodes_from(node_ids)
        self.add_edges_from(map(tuple, edges))
        self.assign_attributes(attributes=attributes)

    def node_to_neighbours(self) -> Dict[int, Set[int]]:
        return {node: set(self.neighbors(node)) for node in self.nodes}

    def node_degrees(self) -> Dict[int, int]:
        return {node: self.degree(node) for node in self.nodes}

    def assign_attributes(self, attributes: pd.DataFrame) -> None:
        nx.set_node_attributes(
            G=self,
            values=dict(zip(attributes["ID"], attributes["attribute"])),
            name="attribute",
        )

    def pair_to_common_neighbour_count(self, node_pairs: np.ndarray) -> Dict[Tuple[int, int], int]:
        node_to_neighbours = self.node_to_neighbours()
        pair_to_count = dict()
        for node_u, node_v in node_pairs:
            shared_neighbours = node_to_neighbours[node_u] & node_to_neighbours[node_v]
            pair_to_count[(node_u, node_v)] = len(shared_neighbours)
        return pair_to_count