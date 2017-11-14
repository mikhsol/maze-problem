import unittest

from maze_problem.solver.maze_solver import MazeSolver
from maze_problem.solver.exceptions import NoInitNodeException


class TestMazeSolver(unittest.TestCase):
    def test_maze_has_init_point(self):
        maze = ('1', '2')
        s = MazeSolver(maze)
        self.assertEqual((0, 0), s.find_init_node())

        maze = ('2', '1')
        s = MazeSolver(maze)
        self.assertEqual((1, 0), s.find_init_node())

        maze = ('20.', '.1.', '0..')
        s = MazeSolver(maze)
        self.assertEqual((1, 1), s.find_init_node())

    def test_maze_has_no_init_point(self):
        maze = ('0', '2')
        s = MazeSolver(maze)
        with self.assertRaises(NoInitNodeException):
            s.find_init_node()
