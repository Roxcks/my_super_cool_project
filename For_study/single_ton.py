class ConfigurationManager:
    __instance = None  # объекта не существует 
    def __new__(cls, *args, **kwargs): 
        if cls.instance is None: # если объекта не существует, то создаст, если есть, вернет объект
            cls.instance = super().__new__(cls) 
            cls._instance._initialized = False
        return cls.__instance
    
    def __init__(self): # задаем инит так, чтобы каждый раз при вызове не сбрасывались значения
        if not self._initialized:
            self._settings = {}
            self._initialized = True # пометили, что инициализация произошла
    
    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        return self._settings.get(key)
#____________________________________________________________________________________
class ConfigurationManager1: # класс, если сразу надо задавать значения атрибутов
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, width=800, height=600):
        # Проверяем, инициализировали ли мы объект раньше
        if not getattr(self, "_initialized", False): # проверяет, существует ли такой аргумент
            self.width = width
            self.height = height
            self._initialized = True  # Ставим флаг, теперь аргумент существует
    # инициализация происходит один первый раз, остальные разы не происходит
#_________________________________________________________________________________
    class ConfigurationManager2: # если хотим каждый раз разные значения задавать
        _instance = None
        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
        def __init__(self, arg1=None, arg2=None):
            if arg1 is not None:
                self.arg1 = arg1
            if arg2 is not None:
                self.arg2 = arg2