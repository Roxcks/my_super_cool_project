class DiaryWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        print('Начало записи...')
        self.file = open(self.filename, "w", encoding="utf-8")
        return self
    def write(self, text):
        if self.file:
            self.file.write(text + '\n')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print('Конец записи.')
            self.file.close()
            print('Новая запись сохранена')
        if exc_type is not None:
            print()
