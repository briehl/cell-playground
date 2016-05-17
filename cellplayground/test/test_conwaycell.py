from cellplayground.conway.cell import (
    ConwayCell,
    State
)
import unittest

class ConwayCellTest(unittest.TestCase):
    # Skips testing Cell.play for the valid case - that gets covered
    # in test_conwayplayground

    def test_good_cell(self):
        c = ConwayCell(loc=[0,0])
        self.assertIsInstance(c, ConwayCell)
        self.assertTrue(c.state is State.DEAD)

    def test_apply_state(self):
        c = ConwayCell(loc=[0,0])
        self.assertTrue(c.state is State.DEAD)
        c.apply_state(State.ALIVE)
        self.assertTrue(c.state is State.ALIVE)

    def test_apply_bad_state(self):
        c = ConwayCell(loc=[0,0])
        with self.assertRaises(ValueError):
            c.apply_state(5)

    def test_str(self):
        c = ConwayCell(loc=[0,0])
        self.assertEqual(str(c), ' ')
        c.apply_state(State.ALIVE)
        self.assertEqual(str(c), '*')

    def test_bad_play(self):
        c = ConwayCell(loc=[0,0])
        with self.assertRaises(ValueError):
            c.play(None)