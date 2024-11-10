# IMPLEMENTING QUEUE  USING LIST

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self, data):
       return self.items.append(data)
            
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('dequeue from empty queue')

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('get_front from empty queue')
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('get_rear from empty queue')
        
    def size(self):
        if not self.is_empty():
            return len(self.items)
        else:
            raise IndexError('size from empty queue')
        
    def display(self):
        if not self.is_empty():
            print(self.items)
        else:
            print('Queue is empty')

Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.display()
Q.dequeue()
Q.display()
print(Q.get_front())
print(Q.get_rear())
print(Q.size())
