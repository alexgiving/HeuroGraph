from collections import defaultdict

import numpy as np

from src.graph import Graph


def color_graph_greedy_randomized_sorted(graph: Graph) -> dict[int, list[int]]:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))

    vertexes_probabilities = [len(graph._data[vertex]) // graph.num_edges for vertex in graph.vertexes]

    randomized_vertexes = np.random.choice(graph.vertexes, graph.num_vertex, p=vertexes_probabilities, replace=False)

    for vertex in randomized_vertexes:
        
        if vertex_colors[vertex]:
            continue

        neighbor_colors = [vertex_colors[neighbor] for neighbor in graph.neighbors(vertex)]

        color = 0
        while True:
            if color not in neighbor_colors:
                vertex_colors[vertex] = color
                break
            else:
                color += 1
    
    result = defaultdict(list)
    for vertex in vertex_colors:
        color = vertex_colors[vertex]
        result[color].append(vertex)
    return dict(result)
