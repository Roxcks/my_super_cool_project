from accessify import protected
import unittest
class DataBaseManager: #создаем синглтон
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @protected
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

class TestDataBaseManager(unittest.TestCase):
    
    def test_singleton(self):
        db1 = DataBaseManager("host1", 1000, 1.0)
        db2 = DataBaseManager("host2", 2000, 2.0)
        self.assertIs(db1, db2)
        self.assertEqual(db1._host, "host2") # Проверяем перезапись

    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            DataBaseManager(port=70000)

    def test_invalid_host(self):
        with self.assertRaises(ValueError):
            DataBaseManager(host=None)

if __name__ == "__main__":
    unittest.main()