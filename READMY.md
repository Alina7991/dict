## Задача: Реализация собственного класса Dict

Описание: Представьте, что в языке Python пропали встроенные словари (dict), и вам нужно создать собственный класс MyDict, который будет вести себя подобно словарю. 

**Класс MyDict должен поддерживать следующие операции:**

**__init__()**: Инициализация пустого словаря.


**__getitem__(key)**: Получение значения по ключу. Если ключ не существует, вернуть None.


**__setitem__(key, value)**: Установка значения по ключу.


**__delitem__(key)**: Удаление элемента по ключу. Если ключ не существует, ничего не делать.


**keys()**: Возвращение списка всех ключей в словаре.


**values()**: Возвращение списка всех значений в словаре.


**items()**: Возвращение списка пар (ключ, значение) в словаре.


**__str__()**: Возврат строкового представления словаря для удобства отладки.

Kод решения задачи:

````
class MyDict:
    def __init__(self):
        self._data = []

    def __setitem__(self, key, value):
        for pair in self._data:
            if pair[0] == key:
                pair[1] = value
                return
        self._data.append([key, value])

    def __getitem__(self, key):
        for pair in self._data:
            if pair[0] == key:
                return pair[1]
        return None

    def __delitem__(self, key):
        for i, pair in enumerate(self._data):
            if pair[0] == key:
                del self._data[i]
                return

    def keys(self):
        return [pair[0] for pair in self._data]

    def values(self):
        return [pair[1] for pair in self._data]

    def items(self):
        return [(pair[0], pair[1]) for pair in self._data]

    def __str__(self):
        return str({key: value for key, value in self.items()})

    def __contains__(self, key):
        return any(pair[0] == key for pair in self._data)

````

Пример использования:
````
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  
print('city' in my_dict)  
del my_dict['age']
print(my_dict.keys())  
print(my_dict.values()) 
````

Вернет:
````
Alice
False
['name']
['Alice']
````