from functions.function import Function
import math


class ParabolicFunction(Function):

    def value(self, x):
        return (0.25 * x)**2 + 4 * math.exp(-0.2 * x**2)

    def derivative(self, x, y):
        return x * (0.125 - 1.6 * math.exp(-0.2 * x**2))

    def __str__(self):
        return "f(x) = (1/4 x)^2-4e^(-1/5 x^2 )-3\tf'(x) = x * (1/8 - 8/5 * math.exp(-1/5 * x^2))"
