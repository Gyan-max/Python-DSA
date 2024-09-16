class Node:
    def __init__(self , prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False

    def insert_at_start(self, data):
        if self.start is None:
            self.start = Node(None, data, None)
        else:
            n = Node(None, data, self.start)
            self.start.prev = n
            self.start = n

    def insert_at_end(self, data):
        if self.is_empty():
            self.start = Node(None, data, None)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data, None)
            temp.next = n


    def search(self, data):
        temp = self.start
        while temp is not None:
           if temp.item == data:
               print(f'{temp.item} is found ')
               break
           temp = temp.next
        else:
            print(f'{data} is not found')


    def insert_after(self, target_data, new_data):
        temp = self.start
        while temp is not None:
            if temp.item == target_data:
                n = Node(temp, new_data, temp.next)
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
                print(f'{new_data} is inserted after {target_data}')
                return
            temp = temp.next
        print(f'{target_data} is not found')
        
    
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            self.start.prev = None


    def delete_last(self):
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        temp = self.start
        if temp.item == data:
            self.start = temp.next
        else:
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
            else:
                print(f'{data} is not found')




mylist = DLL()

mylist.insert_at_start(10)
mylist.insert_at_start(30)
mylist.insert_at_end(50)
mylist.insert_at_end(20)
mylist.insert_at_end(40)
# mylist.search(30)
# mylist.search(80)
# mylist.insert_after(mylist.search(10), 70)
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(50)
mylist.print_all()