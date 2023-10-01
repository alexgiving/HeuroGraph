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
    vertex_colors = dict(zip(graph.vertices, [None] * graph.num_vertex))

    for vertex in graph.vertices:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_sorted(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertices, [None] * graph.num_vertex))
    sorted_vertices = graph.sort()

    for vertex in sorted_vertices:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_randomized_sorted(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertices, [None] * graph.num_vertex))

    vertices_probabilities = [len(graph._data[vertex]) / graph.num_edges / 2 for vertex in graph.vertices]
    randomized_vertices = np.random.choice(graph.vertices, graph.num_vertex, p=vertices_probabilities, replace=False)

    for vertex in randomized_vertices:
        
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result


def color_graph_greedy_sorted_shuffled(graph: Graph) -> ColoringResult:
    vertex_colors = dict(zip(graph.vertices, [None] * graph.num_vertex))
    sorted_vertices = graph.sort_shuffle()

    for vertex in sorted_vertices:
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]
        vertex_colors[vertex] = _get_available_color(neighbor_colors)
    
    result = ColoringResult(vertex_colors)
    return result
