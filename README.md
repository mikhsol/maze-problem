# Maze Problem
Given a maze, find shortest path from initial to destination point.

# Repository
Get repository:
`git clone https://github.com/mikhsol/maze-problem.git maze_problem`

# Running tests
You can run unit tests by:
`python -m unittest`
from the directory above the package.

If you want to see test coverage, need to install coverage package:
`pip install coverage`.
Better use virtual environment.

After package coverage will be installed, run:
`coverage run --source=maze_folder/solver -m unittest discover && coverage report`

# Maze
Maze provided as tuple of strings, where:
* '1' - initial position,
* '2' - destination point,
* '0' - wall
* '.' - road

# Solution
Solution should be provided as list of characters,
which show steps direction should be performed to go
from initial to destination point.

Direction signs:
* 'l' - left
* 'r' - right
* 'u' - up
* 'd' - down

# Examples
```$python
maze1 = (
    '1',
    '2',
)
# result - ['d']

maze2 = (
    '102',
)
# result - excepti0n

maze3 = (
    '1..',
    '00.',
    '...',
    '200',
)
# result - ['r', 'r', 'd', 'd', 'l' , 'l', 'd']

maze4 = (
    '1...0',
    '.00.0',
    '.00.0',
    '...0.',
    '.0...',
    '...0.',
    '.0.0.',
    '00.02',
)
# result - ['d', 'd', 'd', 'r', 'r', 'd', 'r', 'r', 'd', 'd', 'd']
```

