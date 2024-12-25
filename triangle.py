class Triangle:
    def __init__(self, a: float, b: float, c: float):
        _validate_edge(a, "1")
        _validate_edge(b, "2")
        _validate_edge(c, "3")

        if not _is_valid_triangle(a, b, c):
            raise ValueError("The edges do not form a valid triangle.")

        self.a, self.b, self.c = a, b, c

    def calculate_perimeter(self) -> float:
        return self.a + self.b + self.c

def _is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

def _validate_edge(edge: float, edge_name: str):
    if not isinstance(edge, float):
        raise TypeError(f"Edge '{edge_name}' must be a number.")
    if edge <= 0:
        raise ValueError(f"Edge '{edge_name}' must be positive.")
