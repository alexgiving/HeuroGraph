from typing import Callable

import pytest

from heurograph import Graph
from heurograph.coloring import (ColoringResult, color_graph_greedy,
                                 color_graph_greedy_randomized_sorted,
                                 color_graph_greedy_sorted,
                                 color_graph_greedy_sorted_shuffled)


def _validate_coloring(coloring: list[int], graph: Graph) -> bool:
    for vertex_1 in graph.vertices:
        for vertex_2 in graph.neighbors(vertex_1):
            if coloring[vertex_1] == coloring[vertex_2]:
                return False
    return True


testing_functions = [
    color_graph_greedy,
    color_graph_greedy_randomized_sorted,
    color_graph_greedy_sorted,
    color_graph_greedy_sorted_shuffled
    ]

@pytest.mark.coloring
@pytest.mark.parametrize('function', testing_functions)
def test_coloring(function: Callable) -> None:
    graph = Graph()
    graph.make_complete()

    coloring_result: ColoringResult = function(graph)
    if not _validate_coloring(coloring_result.ordered_colors, graph):
        raise ValueError('Solver returns not correct coloring')
