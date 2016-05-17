__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

from Playground.cell import Cell
import unittest

class CellTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_cell_1d(self):
        c = Cell("random", xlim=[-10, 10], ylim=[0,0], zlim=[0,0])
    
    def test_cell_2d(self):
        c = Cell(loc=[1, 1])
        self.assertEqual(c.x, 1)
        self.assertEqual(c.y, 1)
        self.assertEqual(c.z, 0)

    def test_cell_3d(self):
        c = Cell(loc=[1, 1, 1])
        self.assertEqual(c.x, 1)
        self.assertEqual(c.y, 1)
        self.assertEqual(c.z, 1)