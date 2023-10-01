import random

import networkx as nx
import numpy as np

from heurograph.graph import Graph


def nx_clique(graph: Graph) -> list[int]:
    nx_graph = graph.as_nxgraph()
    best_clique = []
    for clique in nx.find_cliques(nx_graph):
        if len(clique) > len(best_clique):
            best_clique = clique
    return best_clique


def greedy_randomized_clique(graph: Graph, iterations: int = 10) -> list[int]:
    best_clique = []
    vertices = graph.vertexes

    for _ in range(iterations):
        clique = []
        random_vertex = random.choice(vertices)

        clique.append(random_vertex)

        vertices_candidates = graph.neighbors(random_vertex)
        np.random.shuffle(vertices_candidates)

        for vertex in vertices_candidates:
            is_connected = True
            for clique_vertex in clique:
                if clique_vertex not in graph.neighbors(vertex):
                    is_connected = False
                    break
            if is_connected:
                clique.append(vertex)
        if len(clique) > len(best_clique):
            best_clique = clique
    return best_clique
