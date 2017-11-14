from maze_problem.solver.node import Node
from maze_problem.solver.exceptions import NoInitNodeException, NoPathException

# possible directions: left, right, down, up
DIRECTIONS = {
    (0, -1): 'l',
    (0, 1): 'r',
    (-1, 0): 'u',
    (1, 0): 'd'
}

class MazeSolver(object):
    def __init__(self, maze=()):
        self.maze = maze
        self.init_node = self._find_init_node()
        self.maze_rows = len(maze)
        self.maze_cols = len(maze[0])

    def _find_init_node(self):
        for row, line in enumerate(self.maze):
            for col, el in enumerate(line):
                if el == '1':
                    return Node('1', row, col)
        raise NoInitNodeException("Wrong maze!")

    def solve(self):
        q = [self.init_node]

        while len(q) != 0:
            n = q.pop(0)
            childes = self._find_childes_nodes(n)
            for child in childes:
                if child.value == '2':
                    return self._construct_path_from_final_node(child)
                q.append(child)

        raise NoPathException("No path in this maze")

    def _find_childes_nodes(self, node):
        return [self._check_position(d, node) for d in DIRECTIONS.keys()
                if self._check_node_availability(d, node)]

    def _check_node_availability(self, direction, node):
        return self.maze_rows > node.row+direction[0] >= 0 \
               and self.maze_cols > node.col+direction[1] >= 0 \
               and self.maze[node.row+direction[0]][node.col+direction[1]] in ['.', '2']

    def _check_position(self, direction, node):
        new_row = node.row+direction[0]
        new_col = node.col+direction[1]
        return Node(self.maze[new_row][new_col], new_row, new_col, node)

    @staticmethod
    def _construct_path_from_final_node(node):
        result = []
        while node.value != '1':
            p = node.prev
            result.append(DIRECTIONS[(node.row-p.row, node.col-p.col)])
            node = node.prev
        return result[::-1]

