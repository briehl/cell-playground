__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

from cell import Cell

class Playground(object):
    """
    An abstract Cell playground.
    """
    def __init__(self, n):
        """
        This default initializer inits with n random cells.
        In general, initializing a Playground should involve adding
        some number of Cells, or at least initing the structure in which
        Cells will exist.
        """
        self.cells = []
        for i in range(0, n):
            self.cells.append(Cell(type="random", xlim=[-10, 10], ylim=[-100, 100], zlim=[-1000, 1000]))

    def play(self):
        """
        Does one step of playing for the Cells in this Playground.
        Should be implemented by subclass to do whatever that calls for.
        """
        print "Playground's open!"
        for c in self.cells:
            print "%d %d %d" % ( c.x, c.y, c.z )

    def neighborhood(self, cell):
        """
        Returns a structure representing the nearest neighborhood
        around the given cell (excluding that cell)
        """
        pass