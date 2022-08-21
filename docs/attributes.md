[⟵](../README.md)
# Атрибуты (`setattr`, `getattr`, `delattr`, `__dict__`)
## `getattr`
Функкия `getattr` позволяет получить значение атрибута по строковому значению атрибута класса:
``` python
    class User:
        name = 'Test'
        age = 17
    
    print(getattr(User, 'name'))
    # 'Test'
```
> При вызове `gettatr(..., ...)()` сразу возвращается значение

Используя третий аргумент можем передать значение по умолчанию
``` python
print(getattr(User, 'surname', 'Null'))
# 'Null'
```

## `setattr`
Функция `setattr` посволяет добавить данные к объекту
``` python
setattr(User, 'surname', 'Petrov')
print(User.surname)
# 'Petrov'
```

## 'delattr`
Функция `delattr` позвозволяет удалить атрибут из класса
``` python
delattr(User, 'name')
print(User.name)
# AttributeError: type object 'User' has no attribute 'name'
```
