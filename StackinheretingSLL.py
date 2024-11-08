#     IMPLEMENTATION OF STACK BY INHERETING SLL CLASS

from SLL import *

class Stack(SLL):
    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        return self.insert_at_start(data)
    
    def pop(self):
        return self.delete_first()
    
    def peek(self):
        return self.start.item
    
    def display(self):
        return self.print_list()
    
    def size(self):
        temp = self.start
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        return count
    

s = Stack()
s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.display()
# s.pop()
s.display()
print(s.peek())
print(s.size())
s.display()