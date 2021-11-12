import pygame
import sys
import math
import matplotlib
import numpy
import problem

"""Define a class for every different type of pathfinding problems"""
class Problem:
    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    def goal_test(self, node):
        return node.state == self.goal.state

    """Returns all available actions from a specific node"""
    def actions(self, node):
        pass

"""Represent the maze problem"""
class Maze(Problem):
    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)

    """Calculate path cost (Or g()) of from initial state to current state"""
    def path_cost(self, node):
        cost = 0
        while node.state != self.initial_state:
            cost += 1
            node = node.parent_node
        return cost

    """Returns the path to get to this node, from initial node"""
    def path(self, node):
        path = [node.state]
        tracker = node.parent
        while node.parent.state !=  self.initial_state:
            path.insert(0, tracker.state)
            tracker = tracker.parent
        return path

    """Return actions"""
    def actions(self, node):
        return node.actions

    """Calculate heuristic for a node, we use Mahattan distance for this one, since I'm not gonna go diagonally """
    def h(self, node):
        return abs(node.state[0] - self.goal.state[0]) + abs(node.state[1] - self.goal.state[1])

""""Represent a node in search problem"""
class Node:
    """Initialize the node in map, cost default is 1 because of the maze problem, can be changed when """
    def __init__(self, state, actions=[], cost=1, parent=None):
        self.state = state          #State is the coordinate of a node.      
        self.actions = actions
        self.parent = parent
        self.cost = cost

    """"Set parent when execute the pathfinding algo."""
    def set_parent(self, parent):
        self.parent = parent

"""Represent every grids on the map for the maze problem"""
class Grid(Node):
    """"Initialize the grid, the actions list is to define all available actions can be done from this grid, cost default is 1, 
    parent can be defined later, when executing the algorithm"""
    def __init__(self, state, width, height, color, actions=[], cost=1, parent=None):
        super().__init__(state, actions, parent, cost)
        self.rect = pygame.Rect(state[0], state[1], width, height)
        self.color_code = numpy.asarray(matplotlib.colors.to_rgb(color))*255
        self.cost = cost

    """Draw this grid on screen"""
    def draw(self, display):
        pygame.draw.rect(display, self.color_code, self.rect)

    """Change color"""
    def change_color(self, color):
        self.color_code = numpy.asarray(matplotlib.colors.to_rgb(color))*255
    
    """Add or delete available actions (Delete when a new obstacle is added)"""
    def update_actions(self, actions, add=True):
        for action in actions:
            if add:
                self.actions.append(action)
            else:
                self.actions.remove(action)