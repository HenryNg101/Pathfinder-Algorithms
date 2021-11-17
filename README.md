# Pathfinder-Algorithms
A pathfinding algorithms visualizer

This application was developed with pygame, is used to visualizer all of pathfinding algorithms (BFS, DFS, A*, etc).

In this program, each grid on map can be expanded in 4 straight directions (For full 8 directions, switch to "master" branch). The purpose is to see the difference between difference informed and uninformed pathfinding algorithms, when each move can has different costs, and shortest path is not necessarily the path that has least moves.

How to use the program:

> python3 game.py

- When starting, set up starting and goal nodes (using mouse). Then, set barricades/walls (using mouse). Then, hit Enter to solve it. Press Escape to escape the program.
- Legends:

    - Red node: Starting node
    - Green node: Goal node
    - Gray nodes: Barricades/Walls
    - Yellow nodes: Explored nodes
    - Blue nodes: Frontier (Potential) nodes