from functools import singledispatch

class User:
    @singledispatch
    def get_value(value):
        print(f'default: {value}')
    
    @get_value.register(int)
    def _(value):
        print(f'int: {value}')

    @get_value.register(str)
    def _(value):
        print(f'str: {value}')

    @get_value.register(bool)
    def _(vallue):
        print(f'bool: {vallue}')
    