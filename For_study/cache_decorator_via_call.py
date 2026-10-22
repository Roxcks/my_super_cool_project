class Cache:
# класс для сохранения кэша 
    def __init__(self, func):
        self.func = func
        self.__cache = {} # словарь для сохранения кэша
    def __call__(self, *args):
        if args in self.__cache:
            print('Достаем результат вычислений из кэша...')
            return self.__cache.get(args)
        else:
            print('Записываем данные нового вычисления в кэш...')
            result = self.func(*args)
            self.__cache[args] = result
            # для кэша не надо использовать метод setdefault(), т.к для того, чтобы он сработал
            # надо все равно вычислять значение выражения справа и тогда теряется смысл кэша
            return self.__cache.get(args)

@Cache
def calculation(x, y):
    if x > 0:
        return x ** y
    else:
        return 'х не может быть отрицательным числом!'

print(calculation(5, 3))
print(calculation(5, 3))