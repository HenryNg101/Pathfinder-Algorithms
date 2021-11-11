"""Define a class for every different type of pathfinding problems"""
class Problem:
    def __init__(self, initial_state, goal, state_space):
        self.initial_state = initial_state
        self.goal = self.goal

     def goal_test(self, node):
        return node.state == goal.state

    """Returns all available actions from a specific node"""
    def actions(self, node):
        return node.actions

"""Represent the maze problem"""
class Maze(Problem):
    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)

    """Returns the path to get to this node, from initial node"""
    def path_cost(node):
        cost = 0
        while node.state != initial_state:
            cost += 1
            node = node.parent_node
        return cost

    """Calculate heuristic for a node, we use Mahattan distance for this one"""
    def h(node):
        return abs(node.state[0] - goal.state[0]) + abs(node.state[1] - goal.state[1])
        

"""Represent every grids on the map"""
class Grid:
    def __init__(self, state, actions, parent):
        self.state = state
        self.actions = actions
        self.path_cost = 0
        self.parent = parent
        
    """Calculate path cost (Or g()) of from initial state to current state"""
    def path_cost(self, node):
        pass
