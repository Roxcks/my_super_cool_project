class DeliveryDrone:
    company = "Python Express"
    total_drones = 0
    def __init__(self, name, max_weight, current_weight=0):
        self.name = name
        self.max_weight = max_weight
        self.current_weight = current_weight
        DeliveryDrone.total_drones += 1
    def load(self, weight):
        if weight < 0:
            print('Вес груза не может быть отрицательным!')
        if weight + self.current_weight <= self.max_weight:
            self.current_weight += weight
            print(f'{self.name}: груз {weight} кг загружен')
        else:
            print(f'{self.name}: недостаточно места')
    def deliver(self):
        print(f'{self.name}: доставлено {self.current_weight} кг')
        self.current_weight = 0
    def show_info(self):
        print(f'Дрон {self.name} | Компания: {self.company} | Груз: {self.current_weight}/{self.max_weight} кг')
    def set_personal_company(self, company):
        self.company = company 
    