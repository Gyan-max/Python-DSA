from SLL import *

class Queue(SLL):
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0

    def is_empty(self):
        if self.mylist.is_empty():
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.item_count += 1
        return self.mylist.insert_at_end(data)

    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        else:
            self.item_count -= 1
            return self.mylist.delete_first()
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("get_front from empty queue")
        else:
            return self.mylist.start.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("get_rear from empty queue")
        else:
            temp = self.mylist.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        
    def size(self):
        return self.item_count
    
    def display(self):
        if not self.is_empty():
            return self.mylist.print_list()
        else:
            raise IndexError('display from empty queue')
        
    

Q = Queue()
Q.enqueue(40)
Q.enqueue(50)
Q.enqueue(60)
Q.display()
Q.dequeue()
Q.display()
print(Q.get_front())
print(Q.get_rear())
print(Q.size())
        
            
