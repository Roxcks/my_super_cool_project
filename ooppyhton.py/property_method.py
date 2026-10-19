class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.__price = price
        self.__discount = discount
    @property #декоратор 
    def price(self): 
        return self.__price
    @price.setter #price становится атрибутом property, setter - метод @property
    def price(self, price):
        if price <= 0:
            raise ValueError ('Цена не может быть меньше или равна 0!')
        self.__price = price
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount):
        if discount < 0 or discount > 50:
            raise ValueError ('Скидка не может быть меньше 0% и больше 50%!')
        self.__discount = discount
    @property #ставим, чтобы метод вызывался без скобок, как остальные методы        
    def final_price(self):
        return self.price * (1 - self.discount / 100)

product1 = Product('патiсiн', 5000, 20)
print(product1.final_price)