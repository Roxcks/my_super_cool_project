class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.calls_count = 0
        self.results_history = []
    def __call__(self, number):
        multiply = self.factor * number
        self.results_history.append(multiply)
        self.calls_count += 1
        return multiply

# Создаем умножитель, который всё удваивает, это ФУНКТОР, его можно вызвать как функцию
# Он передает свое значение в __init__ при создании себя (объекта)
double = Multiplier(factor=2)

new_number = double(5)
# это вызов функции как обычной функции и передачи значения (5 идет в __call__),
# потому что, когда мы вызываем функцию автоматически вызывается __call__
print(new_number)
