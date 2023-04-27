from functions.function import Function
import math


class SinusFunction(Function):

    def value(self, x):
        return math.sin(x)

    def derivative(self, x, y):
        return math.cos(x)

    def __str__(self):
        return "f(x) = sin(x)\t\t\t\t\t\tf'(x) = cos(x)"
