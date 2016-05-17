__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

from cellplayground.playground.cell import Cell
import unittest

class CellTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_cell_1d(self):
        types = ["random", "min", "max"]
        for t in types:
            c = Cell(t, xlim=[-10, 10], ylim=[0,0], zlim=[0,0])
            self.assertIsInstance(c, Cell)

    def test_cell_1d_badtype(self):
        with self.assertRaises(ValueError) as err:
            c = Cell("wut", xlim=[-10,10], ylim=[0,0], zlim=[0,0])

    def test_cell_bad_loc(self):
        with self.assertRaises(ValueError) as err:
            c = Cell(loc=[])
        with self.assertRaises(ValueError) as err:
            c = Cell(loc=[1,2,3,4])

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

    def test_cell_can_play(self):
        c = Cell()
        self.assertTrue(getattr(c, 'play') and callable(c.play))
