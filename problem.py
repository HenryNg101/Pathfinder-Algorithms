import math
import sys

import matplotlib
import numpy
import pygame

"""Calculate distance between one node to another node using Euclidean distance"""
def euclidean_dis(node1, node2):
    return math.sqrt((node1.state[0] - node2.state[0])**2 + (node1.state[1] - node2.state[1])**2)

"""Define a class for every different type of pathfinding problems"""
class Problem:
    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    """Check if the current node is goal or not"""
    def goal_test(self, node):
        return node.state == self.goal.state

    """Returns all available actions from a specific node"""
    def actions(self, node):
        return node.actions

"""Represent the maze problem"""
class Maze(Problem):
    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)

    """Calculate heuristic for a node, we use Mahattan distance for this one, since I'm not gonna go diagonally """
    def h(self, node):
        return euclidean_dis(node, self.goal)

""""Represent a node in search problem"""
class Node:
    """Initialize the node in map, cost default is 1 because of the maze problem, can be changed when """
    def __init__(self, state, actions=[], cost=0, parent=None):
        self.state = state          #State is the coordinate of a node.      
        self.actions = actions
        self.parent = parent
        self.cost = cost

    """"Set parent when execute the pathfinding algo."""
    def set_parent(self, parent):
        self.parent = parent
    
    """Find the path to this node from initial node, also, calculate path cost, known as g()"""
    def path(self, initial_state):
        path = []
        tracker = self.parent
        cost = 0
        #Check if there's any parent from this node, if there's no parent, the value is not Grid object 
        if type(tracker) == Grid:
            cost += euclidean_dis(self, tracker)
        else:
            return path, int(cost)
        while tracker !=  initial_state:
            cost += euclidean_dis(tracker, tracker.parent)
            path.insert(0, tracker)
            tracker = tracker.parent
        return path, int(cost)

"""Represent every grids on the map for the maze problem"""
class Grid(Node):
    """"Initialize the grid, the actions list is to define all available actions can be done from this grid, cost default is 1, 
    parent can be defined later, when executing the algorithm"""
    def __init__(self, state, width, height, color, actions=[], cost=0, parent=None):
        super().__init__(state, actions, parent, cost)
        self.rect = pygame.Rect(state[0], state[1], width, height)
        self.color_code = numpy.asarray(matplotlib.colors.to_rgb(color))*255
        self.color = color
        self.color_setted = False

    """Draw this grid on screen"""
    def draw(self, display):
        pygame.draw.rect(display, self.color_code, self.rect)

    """Change color"""
    def change_color(self, color, solving=False):
        if not solving:
            if not self.color_setted:
                self.color_code = numpy.asarray(matplotlib.colors.to_rgb(color))*255
                self.color = color
                self.color_setted = True
                return self
            else:
                return None
        else:
            self.color_code = numpy.asarray(matplotlib.colors.to_rgb(color))*255
            self.color = color
            self.color_setted = True
            return self