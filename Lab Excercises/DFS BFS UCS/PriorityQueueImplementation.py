class PriorityQueue:

    def __init__(self):
        self.items = []

    def push(self, item, priority):
        self.items.append((priority, item))
        self.items.sort(reverse=True)

    def pop(self):
        return self.items.pop()[1]

    def is_empty(self):
        return len(self.items) == 0