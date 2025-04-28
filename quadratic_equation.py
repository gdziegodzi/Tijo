import math

class NoRealRootsException(Exception):
    pass

class QuadraticEquation:
    """
    Klasa rozwiązująca równania kwadratowe postaci ax^2 + bx + c = 0
    """

    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            raise ValueError("Współczynnik a nie może być zerem w równaniu kwadratowym.")
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self) -> tuple:
        d = self.discriminant()
        if d < 0:
            raise NoRealRootsException("Brak rzeczywistych pierwiastków.")
        elif d == 0:
            x = -self.b / (2 * self.a)
            return (x,)
        else:
            sqrt_d = math.sqrt(d)
            x1 = (-self.b - sqrt_d) / (2 * self.a)
            x2 = (-self.b + sqrt_d) / (2 * self.a)
            return (x1, x2)
