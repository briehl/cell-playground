from cellplayground.playground import init_playground as base_runner
from cellplayground.conway import run_playground as conway_runner

import unittest

class OutsideRunners(unittest.TestCase):
    """
    Kinda redundant, but I WANT 100%!
    """
    def test_conway_runner(self):
        conway_runner(6, 6, 10, 1)

    def test_base_runner(self):
        base_runner(5)