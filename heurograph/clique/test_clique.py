import random

import pytest

from heurograph import Graph
from heurograph.clique import complete_clique


def _validate_clique(clique: list[int], graph: Graph) -> bool:
    for clique_vertex in clique:
        clique_copy = clique.copy()
        clique_copy.remove(clique_vertex)
        for _clique_vertex in clique_copy:
            if _clique_vertex not in graph.neighbors(clique_vertex):
                return False
    return True


@pytest.mark.clique
def test_find_clique() -> None:
    graph = Graph()
    graph.make_complete()
    vertices = graph.vertices

    initial_vertex = random.choice(vertices)
    vertices_candidates = graph.neighbors(initial_vertex)
    initial_clique = [initial_vertex]
    clique = complete_clique(initial_clique, vertices_candidates, graph)
    if not _validate_clique(clique, graph):
        raise ValueError('Solver returns not clique')
