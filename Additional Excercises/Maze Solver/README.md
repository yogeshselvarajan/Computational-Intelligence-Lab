# BFS and DFS Maze Solving Program

This program demonstrates the Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for solving mazes. The maze is represented using ASCII characters, and the program utilizes the turtle module to visualize the maze solving process.

## Maze Representation

The maze is represented using a grid of characters, where the following characters have specific meanings:

- `+`: Wall
- ` `: Path
- `s`: Start position
- `e`: End position

## Data Structures

The program uses the following data structures:

- Queue: A queue data structure is used for BFS, allowing the program to explore cells in a breadth-first manner.
- ExploredSet: An explored set data structure is used to keep track of visited cells during the search process.

## Turtles and Visualization

The turtle module is used to visualize the maze solving process. The following turtle classes are used:

- Maze: Represents the walls of the maze.
- Green: Represents the visited cells during the search.
- Blue: Represents the frontier cells being explored.
- Red: Represents the start position.
- Yellow: Represents the end position and the solution path.

## Program Workflow

1. The maze is initialized by setting up the maze grid and placing the turtles accordingly.
2. The search algorithm is performed, either BFS or DFS, by enqueueing or pushing cells into the queue or stack.
3. During the search, the program visits cells, marks them as visited, and explores neighboring cells.
4. The visited cells are visualized using the green turtle, and the frontier cells are visualized using the blue turtle.
5. Once the end position is reached, the solution path is backtracked using the solution dictionary and visualized using the yellow turtle.

## Screenshots

![Maze Solver BFS](img/maze_solver_bfs.png)
*Example screenshot of the Maze Solver using BFS algorithm.*

![Maze Solver DFS](img/maze_solver_dfs.png)
*Example screenshot of the Maze Solver using DFS algorithm.*

## Usage

To run the program:

1. Install the required dependencies, such as Python and the turtle module.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the repository's directory.
4. Run the program using the command: `python Maze_BFS.py` or `python Maze_DFS.py` depending on which algorithm you want to use.

## Credits

This program was created by [Yogesh S](https://github.com/yogeshselvarajan). Feel free to contribute and improve the code.

