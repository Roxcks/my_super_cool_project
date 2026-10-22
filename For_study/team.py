class Team:
    def __init__(self, name: str, score: int, members: list):
        self.name = name
        self.score = score
        self.members = members
    def __len__(self):
        return len(self.members)
    def __bool__(self):
        return len(self.members) > 0
    def __eq__(self, other):
        return self.score == other.score
    def __lt__(self, other):
        return self.score < other.score
    def __le__(self, other):
        return self.score <= other.score

    # --- Проверка ---
team_a = Team("Alpha", 15, ["Sasha", "Masha"])
team_b = Team("Beta", 20, ["Dima", "Igor", "Lena"])
team_empty = Team("NoName", 0, [])

# Проверяем len()
print(len(team_a))     # Ожидается: 2

# Проверяем bool()
print(bool(team_a))    # Ожидается: True
print(bool(team_empty))# Ожидается: False

# Проверяем сравнения
print(team_a < team_b) # Ожидается: True (15 < 20)
print(team_b > team_a) # Ожидается: True (20 > 15)
print(team_a == team_b)# Ожидается: False