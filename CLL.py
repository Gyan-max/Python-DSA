class Node():
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class CLL():
    def __init__(self, last = None):
        self.last = last

    def is_empty(self):
        if self.last is None:
            print('List is empty')
        else:
            print('List is not empty')

    def insert_at_start(self, data):
        if self.last is None:
            n = Node(data)
            self.last = n
            self.last.next = n
        else:
            n = Node(data)
            n.next = self.last.next
            self.last.next = n

    def _insert_at_end(self, data):
        if self.last is None:
            n = Node(data)
            self.last = n
            self.last.next = n
        else:
            n = Node(data)
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if self.last is None:
            print('List is empty')
        else:
            temp = self.last.next
            while temp is not self.last:
                if temp.item == data:
                    print(f'{data} is found')
                    break
                temp = temp.next
            else:
                if temp.item == data:
                    print(f'{data} is found')
                else:
                    print(f'{data} is not found')
    
    def insert_after(self, target, data):
        if self.last is None:
            print('List is empty')
        else:
            temp = self.last.next
            while True:
                if temp.item == target:
                    n = Node(data)
                    n.next = temp.next
                    temp.next = n
                    if temp is self.last:
                        self.last = n
                    break
                temp = temp.next
                if temp is self.last.next:
                    print(f'{target} is not found')
                    break
        
    def delete_first(self):
        if self.last is None:
            print('List is empty')
        else:
            if self.last.next is self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
                
    def delete_last(self):
        if self.last is None:
            print('List is empty')

        else:
            if self.last.next is self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next
                temp.next = self.last
                self.last = temp

    
    
    def delete_item(self, target):
        if self.last is not None:
            if self.last.next is self.last and self.last.item == target:
                self.last = None
            else:
                temp = self.last.next
                while temp is not self.last:
                    if temp.next.item == target:
                        temp.next = temp.next.next
                        if temp.next is self.last.next:
                            self.last = temp
                            
                        break
                    temp = temp.next
                else:
                    if self.last.item == target:
                        self.delete_last()
                        
                    else:
                        print(f'{target} is not found')


                    
            




    def display(self):
        if self.last is None:
            print('List is empty')
        else:
            temp = self.last.next
            while temp is not self.last:
                print(temp.item , end = ' -> ')
                temp = temp.next    
            print(temp.item)







#driver code

mylist = CLL()
# mylist.is_empty()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
# mylist._insert_at_end(30)
# mylist.search(30)
# mylist.search(40)
# mylist.insert_after(20, 40)
mylist.insert_after(10, 40)

# mylist.delete_first()
mylist.delete_item(40)
mylist.display()