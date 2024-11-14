class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        # self.item_count = 0

    def is_empty(self):
        if self.front is None:
            return True
        else:   
            return False
        
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        # self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            
        # self.item_count -= 1
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError('get_front from empty queue')
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('get_rear from empty queue')
        
    def size(self):
        temp = self.front
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        if not self.is_empty():
            temp = self.front
            while temp is not None:
                print(temp.item, end=' ')
                temp = temp.next
            print()

        else:
            raise IndexError('Not item to display')
        



m = Queue()
m.enqueue(10)
m.enqueue(20)
m.enqueue(30)
m.display()
m.dequeue()
m.display()
print(m.get_front())
print(m.get_rear())
print(m.size())

        


            