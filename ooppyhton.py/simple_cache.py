class SimpleCash: # класс функтор, сохраняет запросы и делает по ним словарь
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args): #принимает в *args кортеж (3,5)
        if args in self.cache: #проверяет был ли уже запрос такой
            print('Достаем из кэша...')
            return self.cache.get(args)
        else:
            print("Считаем тяжелые данные...")
            result = self.func(*args)
            self.cache.setdefault(args, result)
            return result

@SimpleCash # декоратор
def calculator(num1, num2):
    return num1 * num2

print(calculator(3,5))
