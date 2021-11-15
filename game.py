import pygame
import sys
import math
import matplotlib
import numpy
import problem
import solution

def draw_and_update():
    for col in grids:
        for row in col:
            row.draw(main_display)
    for col in range(cols):
        pygame.draw.line(main_display, (0,0,0), (col*30,0), (col*30,height), width=1)
    for row in range(rows):
        pygame.draw.line(main_display, (0,0,0), (0,row*30), (width,row*30), width=1)

    #Update always, so we can see it.
    
    pygame.display.update()

pygame.init()

main_display = pygame.display.set_mode(size=(1680,1050), flags=pygame.NOFRAME)
width, height = pygame.display.get_window_size()
rows = int(height/30)
cols = int(width/30)
grids = []
initial_state = None
goal_state = None

#Create all grids, then add all available actions 
for row in range(rows):
    grid_row = []
    for col in range(cols):
        grid_col = problem.Grid((col*30, row*30), 30, 30, "white")
        grid_row.append(grid_col)    
    grids.append(grid_row)

#Will need to update diagonal moves later. (Or maybe not)
for row in range(rows):
    for col in range(cols):
        actions = []
        top_ok, bottom_ok, left_ok, right_ok = row > 0, row < rows - 1, col > 0, col < cols - 1
        if top_ok:
            #if left_ok:
            #    actions.append(grids[row-1][col-1])
            #if right_ok:
            #    actions.append(grids[row-1][col+1])
            actions.append(grids[row-1][col])
        if bottom_ok:
            #if left_ok:
            #    actions.append(grids[row+1][col-1])
            #if right_ok:
            #    actions.append(grids[row+1][col+1])
            actions.append(grids[row+1][col])
        if left_ok:
            actions.append(grids[row][col-1])
        if right_ok:
            actions.append(grids[row][col+1])
        grids[row][col].actions = actions

#Main game loop
while True:
    main_display.fill((255,255,255))

    #Event checking
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = math.floor(x/30)
            row = math.floor(y/30)
            if initial_state == None:
                initial_state = grids[row][col].change_color("red")
            elif goal_state == None:
                goal_state = grids[row][col].change_color("green")
            else:
                grids[row][col].change_color("gray")
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_ESCAPE]:
                sys.exit()
            elif key_list[pygame.K_KP_ENTER]:
                if initial_state != None and goal_state != None:
                    path = solution.breadth_first_search(initial_state, goal_state, grids, main_display)
                    if path:
                        for node in path:
                            node.change_color("purple", True)
    
    #Drawing all grids and lines
    draw_and_update()