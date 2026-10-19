class DataBaseManager: #создаем синглтон
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    #classmethod для проверки, можно ли создать объект
    def validate_settings(cls, host, port, timeout): 
        if host is None or not isinstance(host, str):
            raise ValueError ('host должно быть строкой!')
        if port is not None:
            if not isinstance(port, (int, float)) or isinstance(port, bool):
                raise TypeError('Порт должен быть числом!')
            if not 1 <= port <= 65535:
                raise ValueError('Порт должен быть в диапазоне от 1 до 65535')
        if timeout is not None:
            if not isinstance(timeout, (int, float)) or isinstance(timeout, bool):
                raise TypeError('Timeout должен быть числом!')
            if not timeout > 0:
                raise ValueError('Timeout должен быть больше 0!')

    def __init__(self, host='localhost', port=5432, timeout=5.0):
        self.validate_settings(host, port, timeout) # проверяем, правильные ли данные
        self._host = host
        self._port = port
        self._timeout = timeout

print("=== ТЕСТ 1: Проверка Singleton ===")
db1 = DataBaseManager(host="localhost", port=5432)
db2 = DataBaseManager(host="127.0.0.1", port=3306)

# Проверяем, что db1 и db2 — это один и тот же объект в памяти
print(f"db1 is db2: {db1 is db2}")  # Должно быть True
print(f"Текущий хост: {db1._host}")   # Должно быть '127.0.0.1' (перезаписалось)


print("\n=== ТЕСТ 2: Проверка валидации (ошибки) ===")

# Проверяем неверный порт (> 65535)
try:
    DataBaseManager(port=99999)
except ValueError as e:
    print(f"Поймали ожидаемую ошибку порта: {e}")

# Проверяем неверный timeout (отрицательный)
try:
    DataBaseManager(timeout=-2)
except ValueError as e:
    print(f"Поймали ожидаемую ошибку таймаута: {e}")

# Проверяем неверный host (не строка, а число)
try:
    DataBaseManager(host=12345)
except ValueError as e:
    print(f"Поймали ожидаемую ошибку хоста: {e}")


print("\n=== ТЕСТ 3: Проверка сохранения старых данных при сбое валидации ===")
# Сначала установим хорошие параметры
db1 = DataBaseManager(host="my_super_db", port=5432)
print(f"Хост до неудачной попытки: {db1._host}")

# Пытаемся передать плохой порт
try:
    DataBaseManager(port="не число")
except TypeError as e:
    print(f"Поймали тип ошибки: {e}")

# Проверяем, остался ли хост прежним (не стерся ли из-за упавшей инициализации)
print(f"Хост после неудачной попытки: {db1._host}")  # Должно остаться 'my_super_db'





