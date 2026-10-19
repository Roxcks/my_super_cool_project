class StringField: # это класс дескриптор
    def __init__(self, name=None): 
        # вызывается в момент создания дескриптора, 
        # сообщаем, что у объекта StringField есть атрибут self.name
        self.name = name
    def __set_name__(self, owner, name): # вызывается в момент создания класса User
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError ('Фамилия и имя должны быть строкой!')
        instance.__dict__[self.name] = value

class User:
    first_name = StringField()
    last_name = StringField()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name