class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self, last = None):
        self.last = last

    def is_empty(self):
        if self.last == None:
            print("List is empty")
        else:
            print("List is not empty")
        
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            self.last = n.next
            self.last.next = n


    def insert_at_end(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            self.last.next = n.next
            self.last.next = n
            self.last = n

    def search(self, data):
        temp = self.last.next
        while temp is not self.last.next:
            if temp.data == data:
                print(f'{data} is found')
                return temp
            temp = temp.next
        print(f'{data} is not found')
        return None
    
    


        

        
            


cll = CircularLinkedList()

cll.insert_at_start(10)