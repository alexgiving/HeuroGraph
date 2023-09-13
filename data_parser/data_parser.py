import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple


def get_pattern() -> Tuple[re.Pattern[str], Tuple[str, ...]]:
    pattern = r'e (?P<vertices_1>\d+) (?P<vertices_2>\d+)'
    pattern_group = ('vertices_1', 'vertices_2')

    compiled_pattern = re.compile(pattern)
    return compiled_pattern, pattern_group


class Parser:
    def __init__(self) -> None:
        self._graph = defaultdict(list)
  
    def read(self, file: Path):
        edge_pattern, edge_group = get_pattern()

        with file.open() as f:
            for data_string in f.readlines():
                if match := edge_pattern.match(data_string):
                    vertex_1 = match.group(edge_group[0])
                    vertex_2 = match.group(edge_group[1])

                    if vertex_2 not in self._graph[vertex_1]:
                        self._graph[vertex_1].append(vertex_2)
                    if vertex_1 not in self._graph[vertex_2]:
                        self._graph[vertex_2].append(vertex_1)



if __name__ == '__main__':
    parser = Parser()
    parser.read(Path('example.col'))
    print(parser._graph)
