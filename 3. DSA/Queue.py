import sys
sys.stdin = open('D:\\Coding Env\\4. PYTHON\\input.txt', 'r')
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')

# Queue
'''<---Implementation of Stack and Queue using Deque--->'''


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert_at_first(self, val):
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(val, self.head, None)
            self.head.prev = node
            self.head = node
            self.size += 1

    def insert_at_last(self, val):
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(val, None, self.tail)
            self.tail.next = node
            self.tail = node
            self.size += 1

    def display(self):
        if not self.isEmpty():
            ptr = self.head
            print('stack or queue elements:')
            while ptr != None:
                print(ptr.data, end="<-->")
                ptr = ptr.next
        else:
            print("List is Empty")
        print()


class Stack(deque):        # used inheritance
    def push(self, val):
        self.insert_at_last(val)


class Queue(deque):        # used inheritance
    def enqueue(self, val):
        self.insert_at_first(val)


stk = Stack()
stk.push(2)
stk.push(6)
stk.push(4)
stk.display()


'''<-----Queue using linked List----->'''


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, val):
        if self.head is None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(val, None, self.tail)
            self.tail.next = node
            self.tail = node
            self.size += 1

    def get(self):
        if self.isEmpty():
            return
        print('Popped items:')
        ptr = self.head
        self.head = ptr.next
        print(ptr.data)
        ptr = None    # unlinked the front node from LL
        self.size -= 1

    def isEmpty(self):
        return self.size == 0

    def qsize(self):
        print('Size of Queue:', self.size)

    def print_(self):
        if self.head is None:
            print("Queue is Empty")
        ptr = self.head
        print('Queue elements:')
        while ptr:
            print(ptr.data, end="<-->")
            ptr = ptr.next
        print()


Q = Queue()
Q.put(5)
Q.put(6)
Q.put(7)
Q.print_()
Q.qsize()
Q.get()
Q.get()
Q.print_()
Q.qsize()
