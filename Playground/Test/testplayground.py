__author__ = "Bill Riehl (briehl@gmail.com)"
__version__ = "0.0.1"
__date__ = "$Date: 2014/07/09 $"

import unittest
from playground import Playground

class PlaygroundTestCase(unittest.TestCase):
    def setUp(self):
        self.num_cells = 2
        self.p = Playground(self.num_cells)

    def test_has_right_number_of_cells(self):
        self.assertEqual(len(self.p.cells), self.num_cells)