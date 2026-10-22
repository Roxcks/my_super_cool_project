import time
class SensorReading:
    __slots__ = ('timestamp', 'sensor_id', 'value')
    def __init__(self, timestamp: str | float, sensor_id: int, value: float):
        self.timestamp = timestamp
        self.sensor_id = sensor_id
        self.value = value
    def __repr__(self):
        return f'SensorReading(timestamp={self.timestamp}, sensor_id={self.sensor_id}, value={self.value})'

class AlertSensorReading(SensorReading): # дочерний класс 
    __slots__ = ('is_alert',) # обязательно нужна запятая в конце, чтобы был кортеж
    def __init__(self, timestamp, sensor_id, value, is_alert):
        super().__init__(timestamp, sensor_id, value)
        self.is_alert = is_alert
    def __repr__(self):
            return f'SensorReading(timestamp={self.timestamp}, sensor_id={self.sensor_id}, value={self.value}, alert={self.is_alert})'

class SensorValueError(Exception):
    # класс определения ошибки
    pass

class ValidatedSensor:
     def __init__(self, value):
        if not -50 <= value <= 100:
            raise SensorValueError('Недопустимое значение температуры')
        self.value = value

try:
    print('Создаем первый датчик...')
    time.sleep(0.5)
    sensor1 = ValidatedSensor(100)
    print('Первый датчик создан')
except SensorValueError as s:
    print(f'Ошибка датчика:{s}')
else:
    print('Датчик создан и соответствует требованиям')
finally:
    time.sleep(0.5)
    print('Работа с датчиками завершена')
