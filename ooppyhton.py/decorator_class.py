class Counter:    # класс декоратор
    
    def __init__(self, func): # принимает функцию plus_calculator
        self.__counter = 0 # счетчик количества вызовов функции
        self.func = func 
    def __call__(self, *args, **kwargs): # принимает функцию plus_calculator(3,5)
        self.__counter += 1
        print(f'Вызов функции номер: {self.__counter}')
        return self.func(*args, **kwargs)

def plus_calculator(num1, num2):
    return num1 + num2

plus_calculator = Counter(plus_calculator) # функция становится объектом класса Counter
print(plus_calculator(3,5))
print(plus_calculator(4,7))
