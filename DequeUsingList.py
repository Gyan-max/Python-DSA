class Deque:
    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            return True
        else:
            return False
        
    def add_front(self, data):
        self.item.insert(0, data)

    def add_rear(self, data):
        self.item.append(data)

    def remove_front(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError('remove_front from empty deque')
        
    def remove_rear(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError('remove_rear from empty deque')
        
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError('get_front from empty deque')
        
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError('get_rear from empty deque')
        
        
    def size(self):
        return len(self.item)
    
    def display(self):
        if not self.is_empty():
            return self.item
        else:
            raise IndexError('Display from empty deque')
        


D = Deque()

D.add_front(10)
D.add_front(20)
D.add_front(30)
D.add_rear(40)
D.add_rear(50)
print(D.display())
D.remove_front()
D.remove_rear()
print(D.display())
print(D.get_front())
print(D.get_rear())
print(D.size())
