class User:
    # def __init__(self, *args, **kwargs) -> None:
    #     self.args = args
    #     self.kwargs = kwargs
    #     print(self.args)
    #     print(self.kwargs)
    def __init__(self, name) -> None:
        self.name = name
        self.print_name()
        
    def print_name(self):
        print(self.name)