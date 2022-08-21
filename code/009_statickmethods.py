class User:
    def __init__(self, name='John', age=20) -> None:
        self.name = name
        self.age = age
        
    def get_data(self):
        print(self.name)
        print(self.age)
    
    @staticmethod
    def get_sum(x, y):
        print(x + y)
