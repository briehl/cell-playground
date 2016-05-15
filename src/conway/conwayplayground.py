from __future__ import print_function
"""
Conway's Game of Life Cell Playground
Simplest Cell Automaton rule keeper. We'll do more like
real biology later.
"""

from playground.playground import Playground
from .conwaycell import (
    ConwayCell,
    State
)
import random

class ConwayPlayground(Playground):
    def __init__(self, w, h):
        """
        w = width, h = height
        """
        self.w = w
        self.h = h
        self.cells = list()
        for i in range(w):
            row = list()
            for j in range(h):
                row.append(ConwayCell(loc=[i,j,0]))
            self.cells.append(row)

    def init_cells(self, num_cells):
        """
        Breathe life into num_cells random Cells.
        """
        for i in range(num_cells):
            flag = False
            while flag is False:
                x = random.randint(0, self.w-1)
                y = random.randint(0, self.h-1)
                if self.cells[x][y].state is State.DEAD:
                    self.cells[x][y].apply_state(State.ALIVE)
                    flag = True

    def play(self):
        """
        1. Iterate over all cells, get their updated state and buffer it.
        2. Apply all new states at once.
        3. Print it out.
        """
        buf = list(self.cells)
        for i in range(self.w):
            for j in range(self.h):
                buf[i][j].apply_state(buf[i][j].play(self))
        self.cells = list(buf)

    def neighborhood(self, row, col):
        """
        Let's make it toroidal, eh?
        """
        neighbors = list()
        horiz_range = self._neighbor_range(col, self.w-1)
        vert_range = self._neighbor_range(row, self.h-1)
        for i in vert_range:
            for j in horiz_range:
                if i is not row and j is not col:
                    neighbors.append(self.cells[i][j])
        return neighbors

    def _neighbor_range(self, around, maximum):
        r = [around-1, around, around+1]
        if r[0] < 0:
            r[0] = maximum
        if r[2] > maximum:
            r[2] = 0
        return r

    def __str__(self):
        reprstr = "ConwayPlayground\n"
        for i in range(self.w):
            for j in range(self.h):
                reprstr += str(self.cells[i][j])
            reprstr += "\n"
        return reprstr