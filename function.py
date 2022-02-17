from math import *
from vector import *


class Function:

    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        # Evaluate the function on the given parameters
        x = None

        if len(args) == 1:
            x = args[0]
        elif len(args) > 1:
            x = args

        return eval(self.funct)

    def __str__(self):
        return f"Function('{self.funct}')"

    def __add__(self, other):
        # Add functions
        return Function(f"{self.funct} + {other.funct}")

    def __sub__(self, other):
        # Subtract functions
        return Function(f"{self.funct} - ({other.funct})")

    def __mul__(self, other):
        # Multiply Functions
        return Function(f"({self.funct}) * ({other.funct})")

    def __truediv__(self, other):
        # Divide Functions
        return Function(f"({self.funct}) / ({other.funct})")

    def composite(self, other):
        # Return a function of a function
        return Function(self.funct.replace("x", f"({other.funct})"))

    @staticmethod
    def staticSlope(x1, y1, x2, y2):
        # Find the slope with given coordinates
        return (y2 - y1) / (x2 - x1)

    def slope(self, x):
        # Find the slope at the given point
        offset = 1e-5
        return Function.staticSlope(x - offset, self(x - offset), x + offset, self(x + offset))

    def slopeFunction(self, x):
        # Create a function for the tangent line at the given point
        slope = self.slope(x)
        return Function(f"(x - {x}) * {slope} + {self(x)}")

    def integralLeft(self, a=0, b=1, n=100):
        # Calculate integral using Left rule
        dx = (b - a) / n
        total = 0

        for i in range(n):
            total += self(a + i * dx) * dx

        return total

    def integralRight(self, a=0, b=1, n=100):
        # Calculate integral using Right rule
        dx = (b - a) / n
        total = 0

        for i in range(n):
            total += self(a + (i + 1) * dx) * dx

        return total

    def integralMidpoint(self, a=0, b=1, n=100):
        # Calculate integral using Midpoint rule
        dx = (b - a) / n
        total = 0

        for i in range(n):
            total += self(a + (i + 0.5) * dx) * dx

        return total

    def integralTrapezoidal(self, a=0, b=1, n=100):
        # Calculate integral using Trapezoidal rule
        dx = (b - a) / n
        total = (dx / 2) * (self(a) + self(b))

        for i in range(1, n):
            total += self(a + i * dx) * dx

        return total

    def integralSimpson(self, a=0, b=1, n=100):
        # Calculate integral using Simpson's rule
        if n % 2 == 1:
            return "Value of 'n' must be even"

        dx = (b - a) / n
        total = (dx / 3) * (self(a) + self(b))

        for i in range(1, n // 2 + 1):
            total += self(a + (2 * i - 1) * dx) * (dx * 4 / 3)

        for i in range(1, n // 2):
            total += self(a + 2 * i * dx) * (dx * 2 / 3)

        return total

    def integralAll(self, a=0, b=1, n=100):
        # Calculate integral using all rules
        return f"Left: {self.integralLeft(a, b, n)}\nRight: {self.integralRight(a, b, n)}\nMidpoint: {self.integralMidpoint(a, b, n)}\nTrapezoidal: {self.integralTrapezoidal(a, b, n)}\nSimpson: {self.integralSimpson(a, b, n)}"

    def series0(self, n=100):
        # Calculate series starting from 0
        total = 0

        for i in range(0, n + 1):
            total += self(i)

        return total

    def series1(self, n=100):
        # Calculate series starting from 1
        total = 0

        for i in range(1, n + 1):
            total += self(i)

        return total

    def iterate(self, list):
        # Return a list of results using the provided list's elements as parameters
        result = []

        for x in list:
            result.append(self(x))

        return result

    @staticmethod
    def API():
        return "Function API:\nFunction + Function\nFunction - Function\nFunction * Function\nFunction / Function\nFunction.composite(Function)\nstaticSlope(x1, y1, x2, y2)\nFunction.slope(x)\nFunction.slopeFunction(x)\nFunction.integralLeft(a, b, n)\nFunction.integralRight(a, b, n)\nFunction.integralMidpoint(a, b, n)\nFunction.integralTrapezoid(a, b, n)\nFunction.integralSimpson(a, b, n)\nFunction.integralAll(a, b, n)\nFunction.series0(n)\nFunction.series1(n)\nFunction.iterate(list)"
