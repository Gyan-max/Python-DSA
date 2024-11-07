#IMPLEMENTATION OF STACK USING SINGLY LINKED LIST

class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Stack():
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        if self.start is None:
            return self.start 

    def push(self, data):
        if not self.is_empty():
            n = Node(data)
            n.next = self.start
            self.start = n
            self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data
            
        else:
            raise IndexError('pop from empty stack')
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('peek from empty stack')
        
    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError('size from empty stack')
        
    def display(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item)
                temp = temp.next
        else:
            raise IndexError('display from empty stack')
        
    def insert_at_last(self, data):
        raise NotImplementedError('Insert at end is not allowed in stack')
    
    def insert_after(self, data):
        raise NotImplementedError('Insert after any node is not allowed in stack')
    
    def delete_item(self):
        raise NotImplementedError('Deletion of element is not allowed in stack')
    
    def reverse(self):
        if not self.is_empty():
            temp = self.start
            prev = None
            while temp is not None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.start = prev
        else:
            raise IndexError('reverse from empty stack')
        
s = Stack()
s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
# s.display()
print('Popped element is : ',s.pop())
s.display()
print("First element of stack is : ",s.peek())
print('Size of stack is :' , s.size())
s.reverse()
s.display()




            
