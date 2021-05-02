# A-Star 8-Puzzle algorithm
## A simple A* algorithm to solve the 8-puzzle game for any valid input states

The 8-puzzle consists of a 3 x 3 board. Eight tiles in the board are numbered from 1 to 8, and one tile is blank.
Any tile adjacent to the blank space can slide into that space. The goal of the game is to reach a given goal
configuration from the given initial state.

This program solves the 8-puzzle game by employing the A* algorithm, as well as allowing the use of 2 different
heuristic cost funtions.
One heuristic is based on the Mahattan distance of each number from its goal position, and the other, less efficient
heuristic is based on the Hamming distance (number of missplaced tiles).

The user can test the system with either chosen start and goal states or randomly generated ones.
