class SpaceShip:
    agency = "Python Space"
    total_ships = 0
    def __init__(self, name, max_fuel, current_fuel=0):
        self.name = name
        self.max_fuel = max_fuel
        self.current_fuel = current_fuel
        SpaceShip.total_ships += 1
    def refuel(self, amount):
        if amount + self.current_fuel <= self.max_fuel:
            print(f'{self.name}: заправлено {amount} ед. топлива')
            self.current_fuel += amount
        else:
            print(f'{self.name}: топливный бак переполнен')
    def fly(self, fuel_cost):
        if self.current_fuel >= fuel_cost:
            self.current_fuel -= fuel_cost
            print(f'{self.name}: полет выполнен, потрачено {fuel_cost} ед. топлива')
        else:
            print(f'{self.name}: недостаточно топлива')
    def show_info(self):
        print(f'Корабль {self.name} | Агентство: {self.agency} | Топливо: {self.current_fuel}/{self.max_fuel}')
    def set_personal_agency(self, agency):
        self.agency = agency