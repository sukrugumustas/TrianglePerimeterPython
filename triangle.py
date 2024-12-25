from typing import List, Union


class Triangle:
    def __init__(self, edges: Union[List[float], tuple[float, float, float]]):
        """
        Initialize a Triangle object with three edges.

        Args:
            edges (list[float] or tuple[float, float, float]): A list or tuple of three edge lengths.

        Raises:
            ValueError: If the number of edges is not 3 or the edges do not form a valid triangle.
            TypeError: If any of the edges is not a number.
        """
        if len(edges) != 3:
            raise ValueError("A triangle must have exactly 3 edges.")

        # Validate each edge is a positive number using all() and list comprehension
        if not all(isinstance(edge, float) and edge > 0 for edge in edges):
            raise TypeError("All edges must be positive numeric values.")

        self.edges = edges

        # Check if edges satisfy the triangle inequality (already implemented correctly)
        if not self.__is_valid_triangle():
            raise ArithmeticError("The edges do not form a valid triangle.")

    def __is_valid_triangle(self) -> bool:
        """
        Check if the edges satisfy the triangle inequality.

        Returns:
            bool: True if the edges form a valid triangle, False otherwise.
        """
        return (
                self.edges[0] + self.edges[1] > self.edges[2] and
                self.edges[1] + self.edges[2] > self.edges[0] and
                self.edges[2] + self.edges[0] > self.edges[1]
        )

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return sum(self.edges)
