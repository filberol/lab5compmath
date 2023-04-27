from functions.function import Function
import math


class SinusSawFunction(Function):

    def value(self, x):
        return (math.sin(2 * x) + 1) ** 3 / 3

    def derivative(self, x, y):
        return 2 * (math.sin(2 * x) + 1) ** 2 * math.cos(2 * x)

    def __str__(self):
        return "f(x) = (sin2x+1)^3 / 3\t\t\t\tf'(x) = 2 (sin(2x)+ 1)^2 * cos(2x)"

