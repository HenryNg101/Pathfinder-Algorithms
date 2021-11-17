
import pygame
import sys
import math
import matplotlib
import numpy
import problem
import solution
from tkinter import messagebox
import tkinter
import time

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

#Hide the tkinter root window, only show message box later on
root_window = tkinter.Tk()
root_window.withdraw()

#Initialize the game, with some beginning variables
pygame.init()

main_display = pygame.display.set_mode(size=(1680,1050), flags=pygame.NOFRAME)
width, height = pygame.display.get_window_size()
rows = int(height/30)
cols = int(width/30)
grids = []
initial_state = None
goal_state = None
mouse_down = False      #Check if the mouse is being clicked and holded or not
problem_not_solved = True       #Check if problem is NOT solved or solved

#Create all grids, then add all available actions 
for row in range(rows):
    grid_row = []
    for col in range(cols):
        grid_col = problem.Grid((col*30, row*30), 30, 30, "white", main_display)
        grid_row.append(grid_col)    
    grids.append(grid_row)

#Add all adjacent nodes of a node to actions of the node.
for row in range(rows):
    for col in range(cols):
        actions = []
        top_ok, bottom_ok, left_ok, right_ok = row > 0, row < rows - 1, col > 0, col < cols - 1
        if top_ok:
            actions.append(grids[row-1][col])
        if bottom_ok:
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
        if event.type == pygame.MOUSEBUTTONDOWN and problem_not_solved:
            x, y = pygame.mouse.get_pos()
            col = math.floor(x/30)
            row = math.floor(y/30)
            mouse_down = True
            if initial_state == None:
                initial_state = grids[row][col].change_color("red")
            elif goal_state == None:
                goal_state = grids[row][col].change_color("green")
            else:
                while mouse_down:
                    grids[row][col].change_color("gray")
                    draw_and_update()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            mouse_down = False
                    x, y = pygame.mouse.get_pos()
                    col = math.floor(x/30)
                    row = math.floor(y/30)
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_ESCAPE]:
                sys.exit()
            if key_list[pygame.K_RETURN] and problem_not_solved:
                if initial_state != None and goal_state != None:
                    path, path_cost, iteration = solution.informed_search(initial_state, goal_state, grids, main_display)
                    
                    #Check this instead of path because nodes are not added to the list until there's a middle node between start and goal node
                    if path_cost > 0:       
                        for node in path:
                            node.change_color("purple", True)
                            time.sleep(0.01)    #For a bit of animation
                            draw_and_update()
                        messagebox.showinfo("Path found", "Total path cost for this path is: " + str(path_cost) + " px\nTotal iteration through frontier list: " + str(iteration))
                    else:
                        messagebox.showerror("Path not found", "Total iteration through frontier list: " + str(iteration))
                    problem_not_solved = False

    #Drawing all grids and lines
    draw_and_update()