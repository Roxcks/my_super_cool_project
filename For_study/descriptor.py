class ValidatedField: 
    # класс дескриптор, который будет проверять класс Player
    def __init__(self, min_value=None, max_value=None, expected_type=None):
        self.min_value = min_value
        self.max_value = max_value
        self.expected_type = expected_type
        self.name = None
    def __set_name__(self, owner, name):
        self.name = name
    # обозначаем, что name это тот level или health, к которому мы обращаемся
    def __get__(self, instance, owner):
        if instance is None:
            return self 
        return instance.__dict__.get(self.name)
    # достаем результат из словаря по ключу self.name
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError('Число находится вне допустимого диапазона!')
        if self.max_value is not None and value > self.max_value:
            raise ValueError('Число находится вне допустимого диапазона!')
        if not self.expected_type is None and not isinstance(value, self.expected_type):
            raise TypeError('Недопустимый формат!')
        instance.__dict__[self.name] = value
    # добавляем в словарь значение по ключу self.name 

class Player:
    level = ValidatedField(min_value=1, max_value=10, expected_type=int)
    health = ValidatedField(min_value=0, max_value=100, expected_type=int)
# записываем сюда ссылки на дескриптор, чтобы значения прошли проверку
    def __init__(self, level, health):
        self.health = health
        self.level = level

player_jane = Player(5, 52)
print(player_jane.__dict__)
player_kate = Player(6,62)
print(player_kate.__dict__)
