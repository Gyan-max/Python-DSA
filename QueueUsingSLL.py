class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.start = None

    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False
        
    def enqueue(self, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(data)
            temp.next = n
            n.next = None

    def dequeue(self):
        if self.start is None:
            print('Queue is empty')
        else:
            if self.start.next is None:
                self.start = None
            else:
                self.start = self.start.next


    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('get_front from empty queue')
        
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        
    def size(self):
        if self.start is None:
            return 0
        else:
            temp = self.start
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()
        else:
            raise IndexError('display from empty queue')    
        


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


