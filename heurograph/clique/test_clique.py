import pytest

from heurograph import Graph
from heurograph.clique import find_clique


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

    clique = find_clique(graph.vertices[0], graph)
    if not _validate_clique(clique, graph):
        raise ValueError('Solver returns not clique')
