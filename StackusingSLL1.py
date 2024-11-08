# IMPLEMENTATION OF STACK BY INHERETING SLL CLASS
from SLL import *

class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0

    def is_empty(self):
        if self.mylist.is_empty():
            
            return True
        else:
            
            return False
        
        
    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    
    def pop(self):
        if not self.is_empty():
            pop_item = self.mylist.start.item
            self.mylist.delete_first()
            self.item_count-=1
            return pop_item
        else:
            raise IndexError('pop from empty stack')
        
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError('peek from empty stack')
        
    def size(self):
        return self.item_count
    
    def display(self):
        if not self.is_empty():
            return self.mylist.print_list()
        
    

#DRIVER CODE

s=Stack()
s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
print(s.peek())
print(s.size())

s.display()