import time
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import pandas as pd

from heurograph import Graph
from heurograph.coloring import (color_graph_greedy_randomized_sorted,
                                 color_graph_greedy_sorted,
                                 color_graph_greedy_sorted_shuffled)


class ResultColumns(Enum):
    INSTANCE = 'Instance'
    TIME = 'Time, s'
    COLORS = 'Colors'
    RESULT = 'Result'

    def __str__(self) -> str:
        return self.value


@dataclass
class CommonParams:
    print_graphs = True
    tests_path = Path('data/coloring')
    save_coloring_path = Path('graphs')
    save_coloring = False


if __name__ == '__main__':

    params = CommonParams()

    result_dict = defaultdict(list)

    test_instances = [
        'myciel3.col',
        'myciel7.col',
        'school1.col',
        'school1_nsh.col',
        'anna.col',
        'miles1000.col',
        'miles1500.col',
        'le450_5a.col',
        'le450_15b.col',
        'queen11_11.col'
        ]
    
    for instance in test_instances:
        instance_path = params.tests_path / instance

        graph = Graph(instance_path)

        coloring_functions = [color_graph_greedy_sorted_shuffled,
                              color_graph_greedy_sorted,
                              color_graph_greedy_randomized_sorted]
        
        best_result = None
        total_coloring_time = 0
        for coloring_function in coloring_functions:

            start_coloring_time = time.time()
            result = coloring_function(graph)
            total_coloring_time += time.time() - start_coloring_time

            if best_result is None:
                best_result = result
                continue
            if result.num_colors < best_result.num_colors:
                best_result = result

        result_dict[ResultColumns.INSTANCE].append(instance)
        result_dict[ResultColumns.TIME].append(round(total_coloring_time, 2))
        result_dict[ResultColumns.COLORS].append(best_result.num_colors)
        result_dict[ResultColumns.RESULT].append(best_result.color_vertices)

        if params.save_coloring:
            params.save_coloring_path.mkdir(parents=True, exist_ok=True)
            graph.visualize(params.save_coloring_path / f'{instance}.png',
                            figsize=(25,25),
                            node_color=best_result.ordered_colors)

    frame = pd.DataFrame(result_dict)
    str_output = frame.to_string(index=False)
    print(str_output)
