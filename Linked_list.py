class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        n_node = Node(data)
        n_node.next = self.head
        self.head = n_node

    def insert_end(self, data):
        n_node = Node(data)
        if not self.head:
            self.head = n_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n_node

    def insert_mid(self, data, pos):
        p1 = pos
        n_node = Node(data)
        if not self.head:
            self.head = n_node
            return
        cur = self.head
        while cur.next:
            pos -= 1
            if pos == 1:
                n_node.next = cur.next
                cur.next = n_node
                return
            cur = cur.next
        print(f'Index: {p1} \nout of range!! ')

    def remove_beg(self):
        cur = self.head
        self.head = cur.next

    def remove_end(self):
        if not self.head:
            print("None")
            return
        if not self.head.next:
            self.head = None
            return

        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def remove_mid(self, pos):
        p1 = pos
        if not self.head:
            print("Empty List !!")
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next:
            pos -= 1
            if pos == 1:
                cur.next = cur.next.next
                return
            cur = cur.next
        print(f'Index: {p1} \nOut of range')

    def display(self):
        cur = self.head
        while cur:
            print(f"{cur.data} -> ", end="")
            cur = cur.next
        print("None")


List = LinkedList()

while True:

    print('1) Insert a node at beg of list.')
    print('2) Insert a node at mid of list')
    print('3) Insert a node at end of list')
    print('4) Remove a node from beg')
    print('5) Remove a node from mid')
    print('6) Remove a node from end')
    print('7) Display List')
    print('8) Exit')

    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        d = int(input("Enter the data (integer) : "))
        List.insert_beg(d)
    if ch == 2:
        d = int(input("Enter the data (integer) : "))
        p = int(input("Enter the position : "))
        List.insert_mid(d, p)
    if ch == 3:
        d = int(input("Enter the data (integer) : "))
        List.insert_end(d)
    if ch == 4:
        List.remove_beg()
    if ch == 5:
        p = int(input("Enter the position : "))
        List.remove_mid(p)
    if ch == 6:
        List.remove_end()
    if ch == 7:
        List.display()
    if ch == 8:
        break








