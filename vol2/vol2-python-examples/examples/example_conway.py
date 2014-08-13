__author__ = 'jheaton'

# for python 3.x use 'tkinter' rather than 'Tkinter'
from Tkinter import *
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_WIDTH = 10
CELL_HEIGHT = 10

# Used to locate the x coordinate of neighbors.
NEIGHBORS_X = [0, 0, 1, -1, -1, 1, -1, 1]

# Used to locate the y coordinate of neighbors.
NEIGHBORS_Y = [1, -1, 0, 0, -1, -1, 1, 1]

class App():
    """
    Conway's game of life.


    """
    def __init__(self):
        self.root = Tk()
        self.c = Canvas(self.root,width=400, height=400)
        self.c.pack()

        rows = CANVAS_HEIGHT / CELL_HEIGHT
        cols = CANVAS_WIDTH / CELL_WIDTH

        self.grid_cells1 = [[0 for x in range(rows)] for x in range(cols)]
        self.grid_cells2 = [[0 for x in range(rows)] for x in range(cols)]

        self.grid_rects = [[None for j in range(cols)] for i in range(rows)]

        for row in range(0,rows):
            for col in range(0,cols):
                x = col * CELL_WIDTH
                y = row * CELL_HEIGHT
                b = bool(random.getrandbits(1))

                self.grid_cells1[row][col] = b
                if b:
                    r = self.c.create_rectangle(x, y, x+CELL_WIDTH,y+CELL_HEIGHT, outline="black", fill="black")
                else:
                    r = self.c.create_rectangle(x, y, x+CELL_WIDTH,y+CELL_HEIGHT, outline="black", fill="white")

                self.grid_rects[row][col] = r

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        rows = CANVAS_HEIGHT / CELL_HEIGHT
        cols = CANVAS_WIDTH / CELL_WIDTH

        for row in range(0,rows):
            for col in range(0,cols):

                total = 0

                for i in range(0,len(NEIGHBORS_X)):
                    n_col = col + NEIGHBORS_X[i]
                    n_row = row + NEIGHBORS_Y[i]
                    if n_col >= 0 and n_col < cols:
                        if n_row >= 0 and n_row < rows:
                            if self.grid_cells1[n_row][n_col]:
                                total=total+1

                alive = self.grid_cells1[row][col]

                if alive:
                    # 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                    if total < 2:
                        alive = False

                    # 2. Any live cell with two or three live neighbors lives on to the next generation. (not needed)
                    # 3. Any live cell with more than three live neighbors dies, as if by overcrowding.
                    if alive and total > 3:
                        alive = False

                else:
                    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if total == 3:
                        alive = True

                self.grid_cells2[row][col] = alive


        for row in range(0,rows):
            for col in range(0,cols):
                r = self.grid_rects[row][col]
                if self.grid_cells2[row][col]:
                    self.c.itemconfig(r, fill="black")
                else:
                    self.c.itemconfig(r, fill="white")

                self.grid_cells1[row][col] = self.grid_cells2[row][col]


        self.root.after(100, self.update_clock)

app=App()