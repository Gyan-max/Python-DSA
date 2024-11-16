class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.start = None

    def is_empty(self):
        if self.start is None:
            print('Deque is empty')
        
    def add_front(self, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            n = Node(data)
            n.next = self.start
            self.start.prev = n
            self.start = n

    def add_rear(self, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(data)
            temp.next = n
            n.prev = temp
            n.next = None

    def delete_front(self):
        if self.start is None:
            print('Deque is empty')
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next

    def delete_rear(self):
        if self.start is None:
            print('Deque is empty')
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def get_front(self):
        if self.start is None:
            print('Deque is empty')
        else:
            return self.start.item
        
    def get_rear(self):
        if self.start is None:
            print('Deque is empty')
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        
    def size(self):
        if not self.start is None:
            temp = self.start
            count = 0
            while temp is not None:
                count += 1
                temp = temp.next
            return count
        else:
            return 0
        
    def display(self):
        if not self.start is None:
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()
        else:
            print('Deque is empty')


D = Deque()

D.add_front(10)
D.add_front(20)
D.add_front(30)
D.add_rear(40)
D.add_rear(50)
print(D.display())
D.delete_front()
D.delete_rear()
print(D.display())
print(D.get_front())
print(D.get_rear())
print(D.size())