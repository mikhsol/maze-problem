from typing import Tuple, List

from maze_problem.solver.node import Node
from maze_problem.solver.exceptions import (
    NoInitNodeException,
    NoPathException,
    NoMazeException,
)

# possible directions: left, right, down, up
DIRECTIONS = {
    (0, -1): 'l',
    (0, 1): 'r',
    (-1, 0): 'u',
    (1, 0): 'd'
}


class MazeSolver(object):
    START = '1'
    FINISH = '2'
    WALL = '0'
    ROAD = '.'

    def __init__(self, maze: Tuple=None):
        if not maze:
            raise NoMazeException("'maze' - is compulsory argument.")
        self.maze = maze
        self.init_node = self._find_init_node()
        self.maze_rows = len(maze)
        self.maze_cols = len(maze[0])
        self.visited_cells = []

    def _find_init_node(self) -> Node:
        for row, line in enumerate(self.maze):
            for col, el in enumerate(line):
                if el == self.START:
                    return Node(self.START, row, col)
        raise NoInitNodeException("Wrong maze!")

    def solve(self) -> List:
        q = [self.init_node]

        while len(q) != 0:
            n = q.pop(0)
            childes = self._find_childes_nodes(n)
            for child in childes:
                if child.value == self.FINISH:
                    return self._construct_path_from_final_node(child)
                q.append(child)
            self.visited_cells.append((n.row, n.col))

        raise NoPathException("No path in this maze")

    def _find_childes_nodes(self, node: Node) -> List:
        return [self._get_next_node(d, node) for d in DIRECTIONS.keys()
                if self._check_node_availability(d, node)]

    def _check_node_availability(self, direction: Tuple[int, int],
                                 node: Node) -> bool:
        next_row = node.row + direction[0]
        next_col = node.col + direction[1]
        return self.maze_rows > next_row >= 0 \
            and self.maze_cols > next_col >= 0 \
            and self.maze[next_row][next_col] in [self.ROAD, self.FINISH] \
            and (next_row, next_col) not in self.visited_cells

    def _get_next_node(self, direction: Tuple[int, int], node: Node) -> Node:
        new_row = node.row + direction[0]
        new_col = node.col + direction[1]
        return Node(self.maze[new_row][new_col], new_row, new_col, node)

    def _construct_path_from_final_node(self, node: Node) -> List:
        result = []
        while node.value != self.START:
            p = node.prev
            result.append(DIRECTIONS[(node.row - p.row, node.col - p.col)])
            node = node.prev
        return result[::-1]
