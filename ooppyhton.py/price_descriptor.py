class PriceField:
    def __init__(self, name=None):
        self.name = name
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Цена должна быть числом!')
        if not value > 0:
            raise ValueError('Цена не может быть меньше 0!')
        instance.__dict__[self.name] = value

class Product:
    price = PriceField()

    def __init__(self, name, price):
        self.name = name
        self.price = price

# Должно работать корректно:
item = Product("Книга", 500)
print(item.price)  # 500

item.price = 750.50
print(item.price)  # 750.5
