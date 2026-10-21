import functools
import time
import random

class Retry:
    def __init__(self, func):
        self.func = func
        self.max_retries = 5
        # Не забываем сохранять метаданные функции
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        attempts = 0  # Локальный счетчик попыток для текущего вызова
        
        while attempts < self.max_retries:
            try:
                return self.func(*args, **kwargs)      
            except Exception as e:
                attempts += 1
                if attempts >= self.max_retries:
                    print(f"❌ Все попытки из ({self.max_retries}) исчерпаны.")
                    raise e
                
                print(f"⚠️ Ошибка: {e}. Пробуем снова (попытка {attempts} из {self.max_retries})...")
                time.sleep(0.5)  # Небольшая пауза перед повтором (опционально)

@Retry
def unstable_api_call():
    # Функция, которая случайно падает в 70% случаев
    if random.random() < 0.7:
        raise ConnectionError("Сетевая ошибка соединения с сервером!")
    return "Данные успешно получены! 🎉"

# Вызываем функцию — она может упасть с первого раза, 
# но декоратор будет автоматически её пересдавать (до 3 попыток)
try:
    result = unstable_api_call()
    print(result)
except ConnectionError as e:
    print(f"❌ Все попытки исчерпаны. Окончательный сбой: {e}")