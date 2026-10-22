class SmartList:
# класс, который добавляет элементы в список, даже если индекс выходит за рамки списка
    def __init__(self, initial_data=None):
        self.data = initial_data if initial_data is not None else []
    def __repr__(self):
        return f'SmartList(data={self.data})'
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, key, value):
        if key >= len(self.data):
            extention = key - len(self.data) + 1
            self.data.extend([None] * extention)
        self.data[key] = value
    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return SmartListIterator(self)

class SmartListIterator:
    def __init__(self, smart_list):
        self._smart_list = smart_list
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index >= len(self._smart_list):
            raise StopIteration
        value = self._smart_list[self._index]
        self._index += 1
        return value
    

# --- Проверка ---
my_list = SmartList([1, 2, 3])

# 1. Проверяем чтение (__getitem__)
print(my_list[1])      # Ожидается: 2

# 2. Проверяем обычную перезапись (__setitem__)
my_list[0] = 99
print(my_list)         # Ожидается: SmartList([99, 2, 3])

# 3. Проверяем АВТОРАШИРЕНИЕ (__setitem__ по несуществующему индексу)
my_list[5] = "сюрприз"
print(my_list)         # Ожидается: SmartList([99, 2, 3, None, None, 'сюрприз'])
print(len(my_list))    # Ожидается: 6

# 4. Проверяем удаление (__delitem__)
del my_list[1]
print(my_list)         # Ожидается: SmartList([99, 3, None, None, 'сюрприз'])
    