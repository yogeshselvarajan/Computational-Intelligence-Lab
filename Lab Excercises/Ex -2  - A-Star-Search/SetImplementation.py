class ExploredSet:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def __contains__(self, item):
        return item in self.items
    