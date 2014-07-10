__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

from cell import Cell
import unittest

class CellTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_random_cell(self):
        c = Cell("random", xlim=[-10, 10], ylim=[0,0], zlim=[0,0])
        