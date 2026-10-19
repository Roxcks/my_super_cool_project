class Player:
    # Конструктор класса: вызывается автоматически при создании нового игрока
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # Метод для отображения информации
    def show_info(self):
        print(f"Игрок: {self.name}, Здоровье: {self.health}")

    # Метод для получения урона
    def take_damage(self, amount):
        print(f"Слова игрока {self.name} неправильно интерпретированы, получает {amount} ед. урона!")
        
        # Меняем атрибут именно того игрока, который вызвал метод
        self.health = self.health - amount
        
        print(f"Оставшееся здоровье: {self.health}")

# 1. Подготовка (теперь данные передаются сразу в конструктор)
warrior = Player("Надя", 100)
mage = Player("Валя", 100)

# 2. Проверяем исходное состояние
warrior.show_info() 
mage.show_info()    

print("--- Битва начинается! ---")

# 3. Атакуем ТОЛЬКО воина
warrior.take_damage(15) 

print("---")

# 4. Проверяем состояние обоих после атаки
warrior.show_info()
mage.show_info()