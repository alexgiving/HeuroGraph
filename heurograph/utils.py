from heurograph import Graph


def sort_vertices_by_neighbors(vertices: list[int], graph: Graph, descending: bool = False) -> list[int]:
    return sorted(vertices, key=lambda vertex: len(graph.neighbors(vertex)), reverse=descending)
