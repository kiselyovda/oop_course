class Test:
    # def __new__(cls, *args, **kwargs):
    #     print('Creating a new instance of the class')
    #     # instance = super(Test, cls).__new__(cls)
    #     instance = super().__new__(cls)
    #     return instance

    def __init__(self, name) -> None:
        print('Attribut initiolization')
        self.name = name

a = Test.__new__(Test)