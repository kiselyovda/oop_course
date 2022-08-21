class User:
    def __init__(self, name='John') -> None:
        self._name = name
    
    @property
    def name(self):
        print('retutned attribute value')
        return self._name
    
    @name.setter
    def name(self, value):
        print('attribute changed')
        self._name = value
        
    @name.deleter
    def name(self):
        print('attribute deleted')
        del self._name