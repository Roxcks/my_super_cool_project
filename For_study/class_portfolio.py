class Portfolio:
    def __init__(self, owner: str, assets: list):
        self.owner = owner
        self.assets = assets
    def __repr__(self):
        return f'Portfolio(owner="{self.owner}", assets = {self.assets})'
    def __str__(self):
        return f'Портфель инвестора {self.owner} (активов: {len(self.assets)})'
    def __len__(self):
        return len(self.assets)
    def __abs__(self):
        return sum(abs(num) for num in self.assets)


my_portfolio = Portfolio("Роксана", [500, -150, 300, -50])

# Проверяем repr()
print(repr(my_portfolio))  # Ожидается: Portfolio(owner='Роксана', assets=[500, -150, 300, -50])

# Проверяем str() и print()
print(my_portfolio)        # Ожидается: Портфель инвестора Роксана (активов: 4)

# Проверяем len()
print(len(my_portfolio))   # Ожидается: 4

# Проверяем abs() (сумма модулей: 500 + 150 + 300 + 50 = 1000)
print(abs(my_portfolio))   # Ожидается: 1000