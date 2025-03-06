import unittest


class Calc:

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a/b

    def multiply(self, a, b):
        return a*b


class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        a_number = 2
        b_number = 3
        result = self.calc.add(a_number,b_number)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero()")
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10,0)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None


if __name__ == "__L2Z1__":
    unittest.main()