from .exceptions import NoInitNodeException


class MazeSolver(object):
    def __init__(self, maze=()):
        self.maze = maze

    def find_init_node(self):
        for row, line in enumerate(self.maze):
            for col, el in enumerate(line):
                if el == '1':
                    return row, col
        raise NoInitNodeException("Wrong maze!")
