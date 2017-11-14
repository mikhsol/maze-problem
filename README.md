# Maze Problem
Given a maze, find shortest path from initial to destination point.

# Maze
Maze provided as list of strings, where:
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
    '1o2',
)
# result - exception

maze3 = (
    '1..',
    'oo.',
    '...',
    '2oo',
)
# result - ['r', 'r', 'd', 'd', 'l' , 'l', 'd]

maze4 = (
    '1...o',
    '.oo.o',
    '.oo.o',
    '...o.',
    '.o...',
    '...o.',
    '.o.o.',
    'oo.o2',
)
# result - ['d', 'd', 'd', 'r' 'r', 'd', 'r', 'r', 'd' 'd' 'd']
```
