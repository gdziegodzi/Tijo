import unittest
from quadratic_equation import QuadraticEquation, NoRealRootsException

class TestQuadraticEquation(unittest.TestCase):

    def test_discriminant_should_return_correct_value(self):
        eq = QuadraticEquation(1, -3, 2)
        self.assertEqual(eq.discriminant(), 1)

    def test_solve_should_return_two_roots_when_discriminant_positive(self):
        eq = QuadraticEquation(1, -3, 2)
        roots = eq.solve()
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 2.0)

    def test_solve_should_return_one_root_when_discriminant_zero(self):
        eq = QuadraticEquation(1, -2, 1)
        roots = eq.solve()
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1.0)

    def test_solve_should_raise_exception_when_discriminant_negative(self):
        eq = QuadraticEquation(1, 0, 1)
        with self.assertRaises(NoRealRootsException):
            eq.solve()

    def test_init_should_raise_exception_when_a_is_zero(self):
        with self.assertRaises(ValueError):
            QuadraticEquation(0, 2, 3)

if __name__ == '__main__':
    unittest.main()
