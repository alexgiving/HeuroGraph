import networkx as nx

from heurograph.graph import Graph


def nx_clique(graph: Graph) -> list[int]:
    nx_graph = graph.as_nxgraph()
    best_clique = []
    for clique in nx.find_cliques(nx_graph):
        if len(clique) > len(best_clique):
            best_clique = clique
    return best_clique
