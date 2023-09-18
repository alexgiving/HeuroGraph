from collections import defaultdict

from src.graph import Graph


def color_graph_greedy(graph: Graph) -> dict[int, list[int]]:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))

    for vertex in graph.vertexes:

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


def color_graph_greedy_sorted(graph: Graph) -> dict[int, list[int]]:
    vertex_colors = dict(zip(graph.vertexes, [None] * graph.num_vertex))
    sorted_vertexes = graph.sort()

    for vertex in sorted_vertexes:
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
