class StrictSchemaMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f'Создаем класс: {name}')
        if name != "BaseModel":
            if 'table_name' in attrs: 
                return super().__new__(mcs, name, bases, attrs) 
                # говорим вернуть экземпляр класса mcs (StrictSchemaMeta)
            else:
                raise TypeError(f"Класс {name} должен обязательно содержать атрибут 'table_name'!")