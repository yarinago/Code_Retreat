import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(add(5, -3), 2)

if __name__ == '__main__':
    unittest.main()
