import random

import numpy as np

from heurograph.graph import Graph
from heurograph.utils import sort_vertices_by_neighbors


def complete_clique(clique: list[int], clique_candidates: list[int], graph: Graph) -> list[int]:
    for vertex in clique_candidates:
        is_connected = True
        for clique_vertex in clique:
            if clique_vertex not in graph.neighbors(vertex):
                is_connected = False
                break
        if is_connected:
            clique.append(vertex)
    return clique


def check_clique_escalating_possibility(vertex: int, best_clique: list[int], graph: Graph) -> bool:
    return len(graph.neighbors(vertex)) > len(best_clique)


def randomized_clique(graph: Graph, iterations: int = 10) -> list[int]:
    best_clique = []
    vertices = graph.vertices

    for _ in range(iterations):
        initial_vertex = random.choice(vertices)
        if not check_clique_escalating_possibility(initial_vertex, best_clique, graph):
            continue

        vertices_candidates = graph.neighbors(initial_vertex)
        initial_clique = [initial_vertex]
        np.random.shuffle(vertices_candidates)

        clique = complete_clique(initial_clique, vertices_candidates, graph)
        if len(clique) > len(best_clique):
            best_clique = clique
    return best_clique


def greedy_clique(graph: Graph, iterations: int = 10) -> list[int]:
    best_clique = []
    sorted_vertices = sort_vertices_by_neighbors(graph.vertices, graph, descending=True)

    for iteration, start_vertex in enumerate(sorted_vertices):
        if iteration > iterations or not check_clique_escalating_possibility(start_vertex, best_clique, graph):
            break
        initial_clique = [start_vertex]
        vertices_candidates = graph.neighbors(start_vertex)
        vertices_candidates = sort_vertices_by_neighbors(vertices_candidates, graph, descending=True)

        clique = complete_clique(initial_clique, vertices_candidates, graph)
        if len(clique) > len(best_clique):
            best_clique = clique
    return best_clique


def greedy_randomized_clique(graph: Graph, iterations: int = 10) -> list[int]:
    best_clique = []
    sorted_vertices = sort_vertices_by_neighbors(graph.vertices, graph, descending=True)

    for start_vertex in sorted_vertices:
        if not check_clique_escalating_possibility(start_vertex, best_clique, graph):
            return best_clique
        for _ in range(iterations):
            initial_clique = [start_vertex]
            vertices_candidates = graph.neighbors(start_vertex)
            np.random.shuffle(vertices_candidates)

            clique = complete_clique(initial_clique, vertices_candidates, graph)
            if len(clique) > len(best_clique):
                best_clique = clique
    return best_clique
