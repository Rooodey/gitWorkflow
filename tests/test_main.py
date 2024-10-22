import unittest
from main import calc

class MainTest(unittest.TestCase):
    def test_00(self):
        self.assertEqual(calc(1, 3), 4)
