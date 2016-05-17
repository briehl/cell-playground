__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

from playground import Playground
from cell import Cell
import sys

def init_playground(num_cells):
    try:
        p = Playground(num_cells)
        p.play()
    except ValueError:
        print "Gotta pass a number!"