import time
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import pandas as pd

from heurograph import Graph
from heurograph.clique import greedy_randomized_clique


class ResultColumns(Enum):
    INSTANCE = 'Instance'
    TIME = 'Time, s'
    CLIQUE = 'Clique size'
    RESULT = 'Clique vertices'

    def __str__(self) -> str:
        return self.value


@dataclass
class CommonParams:
    tests_path = Path('data/clique')


def main():
    params = CommonParams()

    result_dict = defaultdict(list)

    test_instances = [
        'brock200_1.clq',
        'brock200_2.clq',
        'brock200_3.clq',
        'brock200_4.clq',
        'brock400_1.clq',
        'brock400_2.clq',
        'brock400_3.clq',
        'brock400_4.clq',
        'C125.9.clq',
        'gen200_p0.9_44.clq',
        'gen200_p0.9_55.clq',
        'hamming8-4.clq',
        'johnson16-2-4.clq',
        'johnson8-2-4.clq',
        'keller4.clq',
        'MANN_a27.clq',
        'MANN_a9.clq',
        'p_hat1000-1.clq',
        'p_hat1000-2.clq',
        'p_hat1500-1.clq',
        'p_hat300-3.clq',
        'p_hat500-3.clq',
        'san1000.clq',
        'sanr200_0.9.clq',
        'sanr400_0.7.clq'
        ]
    
    for instance in test_instances:
        instance_path = params.tests_path / instance

        graph = Graph(instance_path)
        start_time = time.time()
        result = greedy_randomized_clique(graph, iterations = 10_000)
        total_time = time.time() - start_time

        result_dict[ResultColumns.INSTANCE].append(instance)
        result_dict[ResultColumns.TIME].append(round(total_time, 2))
        result_dict[ResultColumns.CLIQUE].append(len(result))
        result_dict[ResultColumns.RESULT].append(result)

    frame = pd.DataFrame(result_dict)
    str_output = frame.to_string(index=False)
    print(str_output)


if __name__ == '__main__':
    main()
