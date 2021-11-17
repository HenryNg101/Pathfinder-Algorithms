# Pathfinder-Algorithms
A pathfinding algorithms visualizer

This application was developed with pygame, is used to visualizer all of pathfinding algorithms (BFS, DFS, A*, etc).

In this program, each grid on map can be expanded in 8 directions (For 4 straight directions, switch to "no-diagonal" branch). The purpose is to see the difference between difference informed and uninformed pathfinding algorithms, when each move can has different costs, and shortest path is not necessarily the path that has least moves.

How to use the program:

> python3 game.py

- When starting, set up starting and goal nodes (using mouse). Then, set barricades/walls (using mouse). Then, hit Enter to solve it. Press Escape to escape the program.
- Legends:

    - Red node: Starting node
    - Green node: Goal node
    - Gray nodes: Barricades/Walls
    - Yellow nodes: Explored nodes
    - Blue nodes: Frontier (Potential) nodes

Testing result on one example input for different algorithms:

- BFS (Breadth-First Search):

![Visualize](https://github.com/HenryNg101/Pathfinder-Algorithms/blob/master/Images/BFS.png)

    Cost: 2711 px
    Iteration: 1798

- Greedy Best-First Search:

![Visualize](https://github.com/HenryNg101/Pathfinder-Algorithms/blob/master/Images/Greedy%20Best-First%20Search.png)

    Cost: 2259 px
    Iteration: 83

- A*:

![Visualize](https://github.com/HenryNg101/Pathfinder-Algorithms/blob/master/Images/A*.png)

    Cost: 2125 px
    Iteration: 530

- Uniform-cost search:

![Visualize](https://github.com/HenryNg101/Pathfinder-Algorithms/blob/master/Images/Uniform-cost%20Search.png)

    Cost: 2090 px
    Iteration: 1835

> Note: Iteration here is the number of iteration through frontier (reachable nodes from any node) list through expansion, before the algorithm reachs the goal.
