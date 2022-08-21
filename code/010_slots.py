class User:
    __slots__ = ['name', 'age']
    def __init__(self, name='John', age=20) -> None:
        self.name = name
        self.age = age
