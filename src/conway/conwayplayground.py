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

    def init_fun_stuff(self):
        if self.w < 6 or self.h < 6:
            return
        self.cells[2][2].apply_state(State.ALIVE)
        self.cells[2][3].apply_state(State.ALIVE)
        self.cells[2][4].apply_state(State.ALIVE)
        self.cells[3][1].apply_state(State.ALIVE)
        self.cells[3][2].apply_state(State.ALIVE)
        self.cells[3][3].apply_state(State.ALIVE)

    def play(self):
        """
        1. Iterate over all cells, get their updated state and buffer it.
        2. Apply all new states at once.
        3. Print it out.
        """
        buf_states = list()
        for i in range(self.w):
            buf_row = list()
            for j in range(self.h):
                buf_row.append(self.cells[i][j].play(self))
            buf_states.append(buf_row)
        for i in range(self.w):
            for j in range(self.h):
                self.cells[i][j].apply_state(buf_states[i][j])

    def neighborhood(self, row, col):
        """
        Let's make it toroidal, eh?
        Actual spot = (row, col), ignore that one
        """
        neighbors = list()
        horiz_range = self._neighbor_range(col, self.w-1)
        vert_range = self._neighbor_range(row, self.h-1)
        for i in vert_range:
            for j in horiz_range:
                if i is row and j is col:
                    continue
                else:
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
        reprstr = "+" + "".join(["-"] * self.h) + "+\n"
        for i in range(self.w):
            reprstr += "|"
            for j in range(self.h):
                reprstr += str(self.cells[i][j])
            reprstr += "|\n"
        reprstr += "+" + "".join(["-"] * self.h) + "+\n"
        return reprstr
