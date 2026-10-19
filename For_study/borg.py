class AppSettings:
# моносостояние: создается общий словарь атрибутов (состояния)
    _shared_state = {"VERSION": "1.0.0",
        "API_KEY": "secret_key_12345",
        "THEME": "light"}
    def __init__(self, **kwargs):
        super().__setattr__('__dict__', self._shared_state)
        #вызываем метод у базового класса, потому что в этом классе он переопределен
        #не пишем self, он сам передается при вызове super()
        #перенаправляет ссылку с __dict__ на общий словарь _shared_state
        for key, value in kwargs.items():
            upper_key = key.upper()
            setattr(self, upper_key, value)
    def __setattr__(self, name, value):
        if name.upper() in ('VERSION', 'API_KEY'):
            raise PermissionError('Нельзя перезаписывать системные константы!')
        self.__dict__[name.upper()] = value
    def __getattr__(self, name): # срабатывает только когда не найден атрибут
        raise AttributeError(f'атрибут {name} не найден!')
    def __delattr__(self, name):
        if name.upper() in ('VERSION', 'API_KEY'):
            # пишем так, а не name = .. or .. т.к любая строка дает True
            raise PermissionError('Нельзя удалять системные константы!')
        
        # Удаляем атрибут из общего словаря, если он там есть
        if name.upper() in self.__dict__:
            del self.__dict__[name.upper()]
        else:
            raise AttributeError(f'Атрибут {name} не найден!')

s1 = AppSettings(THEME='Blue')
s2 = AppSettings()
s3 = AppSettings(theme='green')

print("Словарь s1:", s1.__dict__)
print("Словарь s2:", s2.__dict__)

# Проверяем, один ли это объект словаря в памяти:
print("Один и тот же словарь?", s1.__dict__ is s2.__dict__)
        
