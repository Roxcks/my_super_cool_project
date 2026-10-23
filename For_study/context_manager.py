import time
import copy
class SafeStateSandbox:
    def __init__(self, data: dict, operation: str):
        self.data = data
        self.operation = operation
        self.start_time = 0
        self.operation_time = 0
    def __enter__(self):
        self._backup = copy.deepcopy(self.data) # делает глубокую копию со всеми вложенными словарями
        self.start_time = time.perf_counter()
        return self.data
    def __exit__(self, exc_type, exc, tb):
        end_time = time.perf_counter()
        self.operation_time = end_time - self.start_time
        if exc_type is not None:
            self.data.clear()
            self.data.update(self._backup) # делаем откат к правильной версии словаря
            print(f'Произошла ошибка {exc_type}: {exc}. Время работы программы: {self.operation_time} секунд')
            return False
        else: 
            print(f'Работа с программой завершена успешно, время выполнения: {self.operation_time} секунд')

user_settings = {'user': 'genius', 'theme': "dark"}

try:
    with SafeStateSandbox(user_settings, "Опасное обновление") as settings:
        settings["theme"] = "neon"  # Сначала меняем
        print(f"Внутри блока (до ошибки): {settings}")
        
        # Происходит ошибка
        raise TypeError("Неверный тип данных передан в настройки!")
except TypeError:
    print("Вне менеджера: перехватили ошибку падения.")

# Проверяем, откатилось ли состояние обратно к исходному ("dark")!
print(f"После проваленного блока: {user_settings}")
    
        
        
    