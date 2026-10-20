class Accumulator:
    def __init__(self, start=0):
        self.total = start
        self.history = []
        self.call_counts = 0
    def __call__(self, value):
        self.total += value
        self.call_counts += 1
        self.history.append(value)
        return self.total

acc = Accumulator(start=10)

print(acc(5))  # Выведет: 15 (10 + 5)
print(acc(3))  # Выведет: 18 (15 + 3)
print(acc(2))  # Выведет: 20 (18 + 2)

print(f"Количество вызовов: {acc.call_counts}")  # Выведет: 3
print(f"История: {acc.history}")  # Выведет: [5, 3, 2]

