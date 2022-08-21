[⟵](../README.md)
# `__len__`, `__str__`, `__repr__`

``` python
class User:
    def __init__(self, value='test') -> None:
        self.value = value
        
    def __len__(self) -> int:
        return len(self.value)

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f'<{self.value} object>'
```

Метод `__len__` возвращает количество символов переданного атрибута.
Метод `__str__` возвращает значение атрибута. Используют для вывода информации о классе или объекте.
Метод `__repr__` возвращает объект. Используется для вывода отладочной информации.