import sys
import os

class Maze(object):

    def __init__(self, filename):
        self.char_array = []
        self.cells = []

        self.prizes = []
        self.start_cell = None

        with open(filename, 'r') as input_file:
            for line in input_file:
                self.char_array.append([ch for ch in line.strip()])

        #Parse the characters into cells with row, column, and type
        for row_num, row in enumerate(self.char_array):
            self.cells.append([])
            for col_num, cell_ch in enumerate(row):
                new_cell = Cell(self, row_num, col_num, CELL_TYPE_MAP[cell_ch])
                if new_cell.cell_type == CELL_PRIZE:
                    self.prizes.append(new_cell)
                elif new_cell.cell_type == CELL_START:
                    self.start_cell = new_cell

                self.cells[row_num].append(new_cell) 
                

    def get_cell(self, row, col):
        if row < 0 or row >= len(self.cells) or col < 0 or col >= len(self.cells[0]):
            return None
        else:
            return self.cells[row][col]

    def get_num_rows(self):
        return len(self.cells)
    
    def get_num_cols(self): 
        return len(self.cells[0])

class Cell(object):
	
    CELL_EMPTY = 0
    CELL_WALL = 1
    CELL_PRIZE = 2
    CELL_START = 3

    CELL_TYPE_MAP = {
        " ": CELL_EMPTY,
        "%": CELL_WALL,
        ".": CELL_PRIZE,
        "P": CELL_START
    }

    def __init__(self, maze, row, col, cell_type):
        self.maze = maze
        self.row = row
        self.col = col
        self.cell_type = cell_type

    def get_north(self):
        return self.maze.get_cell(self.row - 1, self.col)
        
    def get_south(self):
        return self.maze.get_cell(self.row + 1, self.col)
    def get_east(self):
        return self.maze.get_cell(self.row, self.col + 1)

    def get_west(self):
        return self.maze.get_cell(Self.row, self.col - 1)

    def get_neighbors(self):
        return [self.get_north(), self.get_south(), self.get_east(), self.get_west()]

    def __str__(self):
        return "cell: row={}, col={}, type={}".format(self.row, self.col, self.cell_type)
