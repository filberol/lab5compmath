class StateManager:
    __functions = None
    __commands = None

    def get_functions(self):
        return self.__functions

    def set_functions(self, functions):
        self.__functions = functions

    def get_commands(self):
        return self.__commands

    def set_commands(self, comm_list):
        self.__commands = comm_list
