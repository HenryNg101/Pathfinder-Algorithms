import collections
import problem
import pygame
import heapq

#This one I borrowed code and modify from here: https://github.com/aimacode/aima-python/blob/master/utils.py
class PriorityQueue:
    def __init__(self, order='min', f=lambda x: x):
        self.heap = []
        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError(" rder must be either 'min' or 'max'.")

    def append(self, item):
        """Insert item at its correct position."""
        self.heap.append(item)
        self.heap.sort(key=self.f)
    
    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return self.heap.pop(0)
    
    def index(self, element):
        return self.heap.index(element)

def draw_and_update(grids, main_display):
    width, height = pygame.display.get_window_size()
    rows = int(height/30)
    cols = int(width/30)
    for col in grids:
        for row in col:
            row.draw(main_display)
    for col in range(cols):
        pygame.draw.line(main_display, (0,0,0), (col*30,0), (col*30,height), width=1)
    for row in range(rows):
        pygame.draw.line(main_display, (0,0,0), (0,row*30), (width,row*30), width=1)

    #Update always, so we can see it.
    
    pygame.display.update()

def breadth_first_search(initial_state, goal_state, grids, main_display):

    maze = problem.Maze(initial_state, goal_state)

    if maze.goal_test(initial_state):
        return maze.path(initial_state), maze.path_cost(initial_state)

    #Initialize the frontier with initial state
    frontier = collections.deque([initial_state])

    explored = []

    iter = 0
    while frontier:
        node = frontier.popleft()
        if node in explored:       #Remove repetitive nodes that has been explored
            continue
        if node != initial_state:
            node.change_color("yellow", True)       #Change color of explored node to yellow
        explored.append(node)

        for action in maze.actions(node):
            if action not in explored and action.color != "gray":
                action.set_parent(node)
                if maze.goal_test(action):
                    return maze.path(action), maze.path_cost(action), iter
                action.change_color("blue", solving=True)
                #draw_and_update(grids, main_display)
                frontier.append(action)
        draw_and_update(grids, main_display)
        iter += 1

    return False, 0, iter

def best_first_search(initial_state, goal_state, grids, main_display):

    maze = problem.Maze(initial_state, goal_state)

    if maze.goal_test(initial_state):
        return maze.path(initial_state), maze.path_cost(initial_state)

    #Initialize the frontier with initial state
    frontier = PriorityQueue('min', lambda node: abs(node.state[0] - goal_state.state[0]) + abs(node.state[1] - goal_state.state[1]))
    frontier.append(initial_state)

    explored = []

    iter = 0
    while frontier:
        node = frontier.pop()
        if node in explored:       #Remove repetitive nodes that has been explored
            continue
        if maze.goal_test(node):
            return maze.path(node), maze.path_cost(node), iter
        if node != initial_state:
            node.change_color("yellow", True)       #Change color of explored node to yellow
        explored.append(node)

        for action in maze.actions(node):
            if action.color != "gray" and action not in explored:
                if action in frontier.heap:
                    id = frontier.index(action)
                    if maze.path_cost(action) < maze.path_cost(frontier.heap[id]):
                        del frontier.heap[id]
                        frontier.append(action)
                else:
                    action.set_parent(node)
                    action.change_color("blue", solving=True)
                    frontier.append(action)
        draw_and_update(grids, main_display)
        iter += 1

    return False, 0, iter