from functions.function import Function
import math


class NormalDensityFunction(Function):

    def value(self, x):
        return 2 * math.exp(-0.5 * x**2)

    def derivative(self, x, y):
        return -2 * math.exp(-0.5 * x**2) * x

    def __str__(self):
        return "f(x) = 2e^(-1/2 x^2 )\t\t\t\tf'(x) = -2 e^(-1/2 x^2) * x"
