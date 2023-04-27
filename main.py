from commands import *
from functions import *
from service import StateManager
from terminal_colors import *


def read_command(command_dict):
    input_line = input("-> ").split(" ")
    command_line = input_line.pop(0)
    try:
        command_dict[command_line].execute_command(input_line)
    except KeyError:
        print_c("Unknown command.", Colors.FAIL)


if __name__ == '__main__':
    manager = StateManager()
    functions = [
        sinus.SinusFunction(),
        sinus_saw.SinusSawFunction(),
        normal.NormalDensityFunction(),
        parabola.ParabolicFunction(),
    ]
    commands = {
        "exit": exit.Exit(),
        "list_f": func_list.ListFunctions(manager),
        "help": comm_list.ShowCommands(manager),
        "show": show.ShowPic(),
        "find": find.Find(manager)
    }
    manager.set_functions(functions)
    manager.set_commands(commands)
    while True:
        read_command(commands)
