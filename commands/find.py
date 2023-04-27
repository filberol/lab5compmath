from commands.command import Command
from terminal_colors import *
from time_manager import time_count
from functions.function import Function
from solver import euler_method
import numpy as np
import matplotlib.pyplot as plt


class Find(Command):
    __d_arrangement_count = 10

    def __init__(self, manager):
        Command.__init__(self, manager)

    # function to solve
    # left_b:right_b
    # value in left
    # accuracy
    @time_count
    def execute_command(self, arguments):
        if not self.validate_arguments(arguments):
            return
        try:
            function: Function = self.service.get_functions()[int(arguments[0]) - 1]
            bord = list(map(lambda x: float(x), arguments[1].split(":")))
            f_value = float(arguments[2])
            accuracy = float(arguments[3])
            method: euler_method.DiffEquationsSolve = euler_method.EulerDiffSolve()
        except ValueError:
            print_c("Wrong arguments!", Colors.FAIL)
            return

        try:
            dif = f_value - function.value(bord[0])
            gained_arrange, gained_values = method.solve_diff_equation(function, bord, f_value, accuracy)
            original_dots = list(map(lambda x: function.value(x) + dif, gained_arrange))
            full_arrange = np.arange(bord[0], bord[1] - (abs(gained_arrange[1] - gained_arrange[0])), abs(bord[1] - bord[0]) / 100)
            full_values = list(map(lambda x: function.value(x) + dif, full_arrange))

            # Print plot
            plt.figure()
            plt.grid(True)
            plt.rcParams['lines.markersize'] = 2
            plt.plot(full_arrange, full_values, label="Original function")
            plt.plot(gained_arrange, gained_values, label="Euler function")
            plt.legend()
            for i in range(0, len(gained_arrange)):
                plt.plot([gained_arrange[i], gained_arrange[i]],
                         [gained_values[i], original_dots[i]],
                         color='grey', linestyle='--'
                         )
            plt.plot(gained_arrange, gained_values, 'ro')
            plt.plot(gained_arrange, original_dots, 'bo')
            plt.show()
        except Exception:
            print_c("Calculation error!", Colors.FAIL)

    def validate_arguments(self, arguments):
        if len(arguments) < 4:
            print_c("Usage: find <fun_n> <left_b>:<right_b> <y_0> <accuracy>", Colors.WARNING)
            return False
        if int(arguments[0]) not in range(1, len(self.service.get_functions()) + 1):
            print_c("Invalid function index!", Colors.FAIL)
            return False
        return True

    def __str__(self):
        return "Approximate chosen function by another function on interval"
