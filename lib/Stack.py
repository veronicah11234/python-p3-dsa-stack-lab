class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items)):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1
