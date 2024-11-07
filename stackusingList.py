class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            print('Stack is empty')
            
    def push(self, data):
        self.item.append(data)
        print(f'{data} is pushed to stack')

    def pop(self):
        if len(self.item) == 0:
            print('Stack is empty')
        else:
            return self.item.pop()
            # print(f'{self.item[]} is popped from stack')

    def peek(self):
        if len(self.item) == 0:
            print('Stack is empty')
        else:
            return self.item[-1]

    def size(self):
        if len(self.item) == 0:
            print('Stack is empty')
        else:
            return len(self.item)
        
    def display(self):
        if len(self.item) == 0:
            print('Stack is empty')
        else:
            print(self.item)

    def reverse(self):
        if len(self.item) == 0:
            print('Stack is empty')
        else:
            self.item = self.item[::-1]
            print('Stack is reversed')

    
if __name__ == '__main__':
    s = Stack()
    s.is_empty()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.display()
    s.pop()
    s.display()
    print(s.peek())