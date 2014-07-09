from cell import Cell

class Playground:
    """An abstract Cell playground"""
    def __init__(self, n):
        self.cells = []
        for i in range(0, n):
            self.cells.append(Cell("random", [[-10, 10], [-100, 100], [-1000, 1000]]))

    def play(self):
        print "Playground's open!"
        for c in self.cells:
            print "%d %d %d" % ( c.x, c.y, c.z )