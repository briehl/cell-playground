from __future__ import print_function
"""
Conway's Game of Life based Cell.
"""
from aenum import Enum
from playground.cell import Cell

State = Enum('State', 'DEAD ALIVE')

class ConwayCell(Cell):
    state = State.DEAD
    def __init__(self, **kwargs):
        super(ConwayCell, self).__init__(**kwargs)

    def play(self, playground):
        """
        Plays along with standard Game of Life rules. Which are:
        1. 2d playground
        2. Look in neighborhood:
            if < 2 neighbors, die (under-population)
            if 2, 3 neighbors, live
            if > 3 die (over-population)
            empty cells get populated if == 3 neighbors
                (but that's handled by the ConwayPlayground)
        """
        num_live_neighbors = 0
        neighbors = playground.neighborhood(self.x, self.y)
        for i in range(len(neighbors)):
            if neighbors[i].state == State.ALIVE:
                num_live_neighbors += 1
        if self.state == State.DEAD and num_live_neighbors == 3:
            return State.ALIVE
        else:
            if num_live_neighbors < 2 or num_live_neighbors > 3:
                return State.DEAD
            else:
                return State.ALIVE

    def apply_state(self, state):
        self.state = state

    def __str__(self):
        if self.state is State.DEAD:
            return " "
        else:
            return "*"