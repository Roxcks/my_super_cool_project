class Dogs:
    _instance = None
    MIN_AGE = 1
    MAX_AGE = 20
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
    @classmethod
    def validate(cls, dog_age):
        return MIN_AGE < dog_age < MAX_AGE