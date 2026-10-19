class RoleField:
    def __init__(self, ourlist):
        self.ourlist = ourlist
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if not isinstance(value, (str)):
            raise TypeError ('Значение должно быть строкой!')
        if value not in self.ourlist:
            raise ValueError ('Значения нет в списке!')
        instance.__dict__[self.name] = value

class User:
    role = RoleField(ourlist = ['admin', 'moderator', 'user'])

    def __init__(self, username, role):
        self.username = username
        self.role = role

# Это должно работать:
u1 = User("Ирина", "tytyt")
print(u1.role) 
