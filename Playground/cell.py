__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

import random

class Cell:
    """A generic (abstract?) Cell class"""
    def __init__(self, type, lims=[[0,0], [0,0], [0,0]]):
        self.x = self.init_pos(type, lims[0])
        self.y = self.init_pos(type, lims[1])
        self.z = self.init_pos(type, lims[2])

    def init_pos(self, type, lim):
        if type == "random":
            return random.randint(lim[0], lim[1])
        elif type == "min":
            return min(lim)
        elif type == "max":
            return max(lim)
        else:
            return 0