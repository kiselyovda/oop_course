class User:
    args = {
        'version': 1,
        'flags': 2
    }
    
    def __init__(self) -> None:
        self.__dict__ = self.args
 