# Pathfinder-Algorithms
A pathfinding algorithms visualizer

This application was developed with pygame, is used to visualizer all of pathfinding algorithms (BFS, DFS, A*, etc).

In this program, each grid on map can be expanded in 4 straight directions (For full 8 directions, switch to "master" branch). For this one, the one that has the shortest amount of moves also has shortest path length, so I would suggest the 8 directions version for better comparision.

How to use the program:

> python3 game.py

- When starting, set up starting and goal nodes (using mouse). Then, set barricades/walls (using mouse). Then, hit Enter to solve it. Press Escape to escape the program.
- Legends:

    - Red node: Starting node
    - Green node: Goal node
    - Gray nodes: Barricades/Walls
    - Yellow nodes: Explored nodes
    - Blue nodes: Frontier (Potential) nodes
    - Purple nodes: The path that was found by the algorithm
