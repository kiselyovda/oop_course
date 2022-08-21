class User:
    version = 1
    
    def __init__(self, name='John') -> None:
        self.name = name
    
    @classmethod
    def set_name(cls, value):
        cls.version = value
