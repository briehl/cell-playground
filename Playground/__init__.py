from playground import Playground
from cell import Cell
import sys

def init_playground():
    try:
        p = Playground(int(sys.argv[1]))
        p.play()
    except ValueError:
        print "Gotta pass a number!"