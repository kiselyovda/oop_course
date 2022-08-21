class User:
    __slots__ = ['__name']
    def __init__(self, name='John') -> None:
        self.__name = name
