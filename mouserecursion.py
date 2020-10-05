#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:19:19 2020

@author: ryanmosenkis
"""
import copy


class Mouse:

    def __init__(self):
        self.boolean = True # variable to check if there are no paths
    
    def find_maze_paths(self, maze, start_row, start_col, exit_row, exit_col):
        ''' function that finds all possible paths from one point to another
        given the start location and the exit location and if there are no 
        paths, prints the appropriate statement
        
        returns nothing
        '''
        self.find_all_paths(maze, start_row, start_col, exit_row, exit_col)
        
        # checking if there are no paths
        if self.boolean == True:
            print("There are no paths")
    
    def find_all_paths(self, maze, start_row, start_col, exit_row, exit_col):
        ''' function that finds all possible paths from one point to another
        given the start location and the exit location
        
        returns nothing
        '''
        local_maze = copy.deepcopy( maze )
        local_maze.set_value(start_row, start_col, '!')
        
        # base case
        if start_row == exit_row and start_col == exit_col:
            print("It's a path!")
            print(local_maze)
            self.boolean = False # there is at least one path if it reaches this
        else: # all other cases
            # checks the space to the north
            if local_maze.get_value(start_row - 1, start_col) == ' ' and \
            local_maze.is_in_maze(start_row - 1, start_col):
                self.find_all_paths(local_maze, start_row - 1, start_col, \
                                     exit_row, exit_col)            
            # checks the space to the south
            if local_maze.get_value(start_row + 1, start_col) == ' ' and \
            local_maze.is_in_maze(start_row + 1, start_col):
                self.find_all_paths(local_maze, start_row + 1, start_col, \
                                     exit_row, exit_col)
            # checks the space to the west
            if local_maze.get_value(start_row, start_col - 1) == ' ' and \
            local_maze.is_in_maze(start_row, start_col - 1):
                self.find_all_paths(local_maze, start_row, start_col - 1, \
                                     exit_row, exit_col)
            # checks the space to the east
            if local_maze.get_value(start_row, start_col + 1) == ' ' and \
            local_maze.is_in_maze(start_row, start_col + 1):
                self.find_all_paths(local_maze, start_row, start_col + 1, \
                                     exit_row, exit_col)