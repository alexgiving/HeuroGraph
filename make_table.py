import time
from collections import defaultdict
from enum import Enum
from pathlib import Path

import pandas as pd

from src.coloring import color_graph
from src.graph import Graph


class ResultColumns(Enum):
    INSTANCE = 'Instance'
    TIME = 'Time, s'
    COLORS = 'Colors'
    RESULT = 'Result'

    def __str__(self) -> str:
        return self.value


if __name__ == '__main__':

    result_dict = defaultdict(list)

    tests_path = Path('tests')
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
        instance_path = tests_path / instance

        graph = Graph()
        graph.read(instance_path)

        start_time = time.time()
        output = color_graph(graph)
        total_time = time.time() - start_time

        number_of_colors = len(output)

        result_dict[ResultColumns.INSTANCE].append(instance)
        result_dict[ResultColumns.TIME].append(total_time)
        result_dict[ResultColumns.COLORS].append(number_of_colors)
        result_dict[ResultColumns.RESULT].append(None)

    frame = pd.DataFrame(result_dict)
    s = frame.to_string()
    print(s)
