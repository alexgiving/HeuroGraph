import numpy as np

from heurograph.coloring.coloring_result import ColoringResult
from heurograph.graph import Graph


def _get_available_color(neighbor_colors: list[int]) -> int:
    color = 0
    while True:
        if color not in neighbor_colors:
            return color
        else:
            color += 1


def color_graph_greedy(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))

    for vertex in graph.vertexes:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_sorted(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))
    sorted_vertexes = graph.sort()

    for vertex in sorted_vertexes:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_randomized_sorted(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))

    vertexes_probabilities = [len(graph._data[vertex]) / graph.num_edges / 2 for vertex in graph.vertexes]
    randomized_vertexes = np.random.choice(graph.vertexes, graph.num_vertex, p=vertexes_probabilities, replace=False)

    for vertex in randomized_vertexes:
        
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_sorted_shuffled(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))
    sorted_vertexes = graph.sort_shuffle()

    for vertex in sorted_vertexes:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result
