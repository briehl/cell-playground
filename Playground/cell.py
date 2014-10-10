__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

import random

class Cell:
    """
    A generic (abstract?) Cell class
    A Cell should be initialized with a location, at least.
    Subclasses of Cell should implement the play() function,
    which does an action for a single step.
    """
    def __init__(self, type, loc=[0,0,0], xlim=[0,0], ylim=[0,0], zlim=[0,0]):
        self.x = self.init_pos(type, xlim)
        self.y = self.init_pos(type, ylim)
        self.z = self.init_pos(type, zlim)

    def init_pos(self, type, lim):
        if type == "random":
            return random.randint(lim[0], lim[1])
        elif type == "min":
            return min(lim)
        elif type == "max":
            return max(lim)
        else:
            return 0