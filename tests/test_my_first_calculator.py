import unittest
from my_first_calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(50, 0), 50)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(50, 50), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(50, 2), 100)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(50, 5), 10)
        self.assertEqual(divide(10, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
