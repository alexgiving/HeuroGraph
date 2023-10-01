from collections import defaultdict


class ColoringResult:
    def __init__(self, vertex_color: dict[int, int]) -> None:
        self._vertex_color = vertex_color
        self._color_vertices = None
    
    def _prepare_result(self) -> dict[int, list[int]]:
        color_vertices = defaultdict(list)
        for vertex in self._vertex_color:
            color = self._vertex_color[vertex]
            color_vertices[color].append(vertex)
        return dict(color_vertices)

    @property
    def color_vertices(self) -> dict[int, list[int]]:
        if not self._color_vertices:
            self._color_vertices = self._prepare_result()
        return self._color_vertices

    @property
    def num_colors(self) -> int:
        return len(self.color_vertices)
    
    @property
    def ordered_colors(self) -> list[int]:
        return list(self._vertex_color.values())
    