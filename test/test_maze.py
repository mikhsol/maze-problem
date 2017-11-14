import unittest

from maze_problem.solver.maze_solver import MazeSolver
from maze_problem.solver.exceptions import NoInitNodeException, NoPathException
from maze_problem.solver.node import Node


class TestMazeSolverInitialisation(unittest.TestCase):
    def test_maze_has_init_point(self):
        maze = ('1', '2')
        s = MazeSolver(maze)
        n = Node('1', 0, 0)
        self.assertEqual(n, s.init_node)

        maze = ('2', '1')
        s = MazeSolver(maze)
        n = Node('1', 1, 0)
        self.assertEqual(n, s.init_node)

        maze = ('20.', '.1.', '0..')
        s = MazeSolver(maze)
        n = Node('1', 1, 1)
        self.assertEqual(n, s.init_node)

    def test_maze_has_no_init_point(self):
        maze = ('0', '2')
        with self.assertRaises(NoInitNodeException):
            MazeSolver(maze)


class TestMazeSolverSolution(unittest.TestCase):
    def test_correct_maze_solver(self):
        maze = ('1', '2')
        s = MazeSolver(maze)
        result = ['d']
        self.assertEqual(result, s.solve())

        maze = ('10', '.2')
        s = MazeSolver(maze)
        result = ['d', 'r']
        self.assertEqual(result, s.solve())

        maze = ('1..', '00.', '...', '200',)
        s = MazeSolver(maze)
        result = ['r', 'r', 'd', 'd', 'l', 'l', 'd']
        self.assertEqual(result, s.solve())

        maze = (
            '1...0',
            '.00.0',
            '.00.0',
            '...0.',
            '.0...',
            '...0.',
            '.0.0.',
            '00.02',
        )
        s = MazeSolver(maze)
        result = ['d', 'd', 'd', 'r', 'r', 'd', 'r', 'r', 'd', 'd', 'd']
        self.assertEqual(result, s.solve())

    def test_maze_has_no_path(self):
        maze = ('102',)
        s = MazeSolver(maze)
        with self.assertRaises(NoPathException):
            s.solve()
