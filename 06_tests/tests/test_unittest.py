import unittest
import sys

from pathlib import Path
path = Path(__file__).parent.parent.resolve()
print(path)
sys.path.append(str(path))

from main import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual((-3.0, -5.0), solution(1, 8, 15))

    def test_2(self):
        self.assertEqual((3.5,), solution(-4, 28, -49))

    def test_3(self):
        self.assertEqual("корней нет", solution(1, 1, 1))