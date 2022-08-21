[⟵](../README.md)
# `__slots__`

Атрибут `__slots__` позволяет сократить использование памяти.
`__slots__` содержит в себе список атрибутов класса и не дает создать новые.
``` python
class User:
    __slots__ = ['name', 'age']
    def __init__(self, name='John', age=20) -> None:
        self.name = name
        self.age = age

obj = User()
obj.another_attr = 1
# AttributeError: 'User' object has no attribute 'another_attr'
```

При наследованиии класса