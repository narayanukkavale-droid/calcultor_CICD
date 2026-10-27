import unittest
from calculator import add,sub,mult,div

class Testcalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(sub(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(mult(10, 5), 50)

    def test_division(self):
        self.assertEqual(div(10, 5), 2.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            div(10, 0)


if __name__ == "__main__":
    unittest.main()
    


