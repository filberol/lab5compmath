from functions.function import Function
from solver.find import DiffEquationsSolve
import numpy as np


def count_values(func, x_arr, y_a):
    values = [y_a]
    last_val = y_a
    dist = abs(x_arr[1] - x_arr[0])
    for x in x_arr[1:]:
        new_val = func.derivative(x, last_val) * dist + last_val
        values.append(new_val)
        last_val = new_val
    return values


class EulerDiffSolve(DiffEquationsSolve):
    __d_arrangement_count = 5

    def solve_diff_equation(self, func: Function, bord, y_a, accuracy):
        dif = y_a - func.value(bord[0])
        gained_accuracy = accuracy + 1
        gained_arrangement = abs(bord[1] - bord[0]) / self.__d_arrangement_count
        gained_values = []
        arrange = []
        while gained_accuracy > accuracy:
            arrange = np.arange(bord[0], bord[1], gained_arrangement)
            gained_values = count_values(func, arrange, y_a)
            euler_val = gained_values[len(gained_values) - 1]
            real_val = func.value(arrange[len(arrange) - 1]) + dif
            gained_accuracy = abs(euler_val - real_val)
            gained_arrangement /= 2
        print("Used " + str(len(arrange)) + " points to achieve accuracy")

        return arrange, gained_values
