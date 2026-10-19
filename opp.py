class Fridge:
    __shared_state = {
        'items': ['сыр', 'молоко']
    }
    def __init__(self):
        self.__dict__ = self.__shared_state
    def add_item(self, item):
        self.items.append(item)
    def check_items(self):
        return self.items
