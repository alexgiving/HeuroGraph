from functools import partial
from multiprocessing import Pool, cpu_count

import numpy as np

from heurograph.graph import Graph


def greedy_randomized_mp_clique(graph: Graph, iterations: int = 10, num_proc: int = -1) -> list[int]:
    raise NotImplementedError('The multiprocessing implementation is under optimization')
    best_clique = []
    vertices = graph.vertices

    random_vertices = np.random.choice(vertices, iterations)
    num_process = num_proc if num_proc > 1 else cpu_count()

    partial_get_clique =  partial(find_clique, graph=graph)
    with Pool(num_process) as pool:
        cliques = pool.map(partial_get_clique, random_vertices)
    best_clique = max(cliques, key=len)
    return best_clique
