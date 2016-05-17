from cellplayground.conway.playground import ConwayPlayground
from cellplayground.conway.cell import State
import unittest

class ConwayPlaygroundTestCase(unittest.TestCase):

    def test_init_playground(self):
        p = ConwayPlayground(5, 5)
        self.assertIsInstance(p, ConwayPlayground)

    def test_init_cells(self):
        w = 5
        h = 5
        p = ConwayPlayground(w, h)
        p.init_cells(10)
        living_cells = 0
        for x in range(w):
            for y in range(h):
                if p.cells[x][y].state is State.ALIVE:
                    living_cells += 1
        self.assertEqual(living_cells, 10)

    def test_init_too_many_cells(self):
        w = 5
        h = 5
        p = ConwayPlayground(w, h)
        p.init_cells(100)
        for x in range(w):
            for y in range(h):
                self.assertEqual(p.cells[x][y].state, State.ALIVE)

    def test_init_fun(self):
        p = ConwayPlayground(6, 6)
        p.init_fun_stuff()
        p = ConwayPlayground(3, 3)
        with self.assertRaises(ValueError):
            p.init_fun_stuff()

    def test_str(self):
        p = ConwayPlayground(6, 6)
        p.init_fun_stuff()
        s = str(p)
        std = ("+------+\n"
               "|      |\n"
               "|      |\n"
               "|  *** |\n"
               "| ***  |\n"
               "|      |\n"
               "|      |\n"
               "+------+\n")
        self.assertEqual(s, std)

    def test_play(self):
        p = ConwayPlayground(6, 6)
        p.init_fun_stuff()
        p.play()
        should_be_alive = [(1,3),(2,1),(2,4),(3,1),(3,4),(4,2)]
        for s in should_be_alive:
            self.assertEqual(p.cells[s[0]][s[1]].state, State.ALIVE)
        self.assertEqual(p.cells[0][0].state, State.DEAD)
        self.assertEqual(p.cells[5][5].state, State.DEAD)
