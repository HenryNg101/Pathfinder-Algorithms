import collections
import problem
import pygame

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
        return maze.path(initial_state)

    #Initialize the frontier with initial state
    frontier = collections.deque([initial_state])

    explored = []

    iter = 0
    while frontier:
        node = frontier.popleft()
        if node in explored:       #Remove repetitive nodes that has been explored
            continue
        print(node.state)
        if node != initial_state:
            node.change_color("yellow", True)       #Change color of explored node to yellow
        explored.append(node)

        for action in maze.actions(node):
            if action not in explored and action.color != "gray":
                action.set_parent(node)
                if maze.goal_test(action):
                    print(iter)
                    return maze.path(action)
                action.change_color("blue", solving=True)
                frontier.append(action)
        draw_and_update(grids, main_display)
        iter += 1
    
    return False