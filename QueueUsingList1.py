# INHERETING LIST CLASS

class Queue(list):
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, data):
        return self.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        
    def size(self):
        if not self.is_empty():
            return len(self)
        
    def display(self):
        if not self.is_empty():
            print(self)

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