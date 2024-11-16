class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            print('List is empty')
        else:
            print('List is not empty')

    def insert_at_start(self, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            n = Node(data)
            self.start.prev = n
            n.next = self.start
            self.start = n

    def insert_at_end(self, data):
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

    def search(self, data):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    print('{data} is found'.format(data=data))
                    break
                temp = temp.next
            else:
                print('{data} is not found'.format(data=data))



    def insert_after(self, target, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            temp = self.start
            while temp is not None:
                if temp.item == target:
                    n = Node(data)
                    n.prev = temp
                    n.next = temp.next
                    temp.next = n
                    break
                temp = temp.next
            else:
                print('Target not found')


    def insert_before(self, target, data):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            temp = self.start
            while temp is not None:
                if temp.item == target:
                    n = Node(data)
                    n.prev = temp.prev
                    n.next = temp
                    temp.prev = n
                    break
                temp = temp.next
            else:
                print('Target not found')

    def delete_first(self):
        if self.start is None:
            print('List is empty')
        else:
            self.start = self.start.next 

    def delete_last(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break
                temp = temp.next
            else:
                print('Item not found')


    def display(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                print(f'{temp.item} ', end=' ')
                temp = temp.next
            print()
    def __len__(self):
        count = 0
        temp = self.start
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def reverse(self):
        if self.start is None:
            print('List is empty')
            return
        current = self.start
        prev_node = None
        while current is not None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.start = prev_node
            

    def sort(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                current = temp.next
                while current is not None:
                    if temp.item > current.item:
                        temp.item, current.item = current.item, temp.item
                    current = current.next
                temp = temp.next

                

# driver code
mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_end(50)
mylist.insert_at_end(60)
# mylist.delete_first()




mylist.display()