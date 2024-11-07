# IMPLEMENTING STACK BY INHERETING LIST CLASS

class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('pop from empty stack')
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('peek from empty stack')
    
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError('size from empty stack')
        
    def display(self):
        if not self.is_empty():
            print(self)
        else:
            raise IndexError('display from empty stack')
        
    def insert(self, index, data):
        raise NotImplementedError('insert is not allowed in stack')
    
    def remove(self, data):
        raise NotImplementedError('remove is not allowed in stack')
    
    def reverse(self):
        if not self.is_empty():
            return self[ ::-1]
        else:
            raise IndexError('reverse from empty stack')
    
s = Stack()
print(s.is_empty())
s.push(10)

s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.display()
print(s.peek())
print(s.size())
print(s.reverse())
