import datetime
from collections import deque
from queue import LifoQueue, Queue
import queue
import sys
sys.stdin = open('D:\\Coding Env\\4. PYTHON\\input.txt', 'r')
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')

# Stack
'''<----------- Applications of stack ----------->'''

'''# 1. reverse a string using stack

sr = 'mayank'
stack = deque()
for i in sr:
    stack.append(i)
ans = ''.join([stack.pop() for i in range(len(stack))])
print('reversed:', ans)


# 2. check for balanced paranthesis

def is_balanced(exp):
    sb = []
    for char in exp:
        if char == '{' or char == '(' or char == '[':
            sb.append(char)
        else:
            if not sb:
                return False
            curr_char = sb.pop()
            if curr_char == '(':
                if char != ')':
                    return False
            if curr_char == '{':
                if char != '}':
                    return False
            if curr_char == '[':
                if char != ']':
                    return False
    if sb:  # # check for empty stack
        return False
    return True


exp = '(]'
if is_balanced(exp):
    print('Balanced')
else:
    print('Unbalanced')'''


'''<-----implementation of stack using queue----->'''

# stack = LifoQueue()
# stack.put('a')
# stack.put('b')
# stack.put('c')
# print(LifoQueue(stack))
# print('queue size :', stack.qsize())
# stack.get()
# stack.get()
# print(stack)
# print('queue size after get :', stack.qsize())


'''1. <-----making pop operation costly----->'''


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.put(item)

    def pop(self):
        if self.q1.qsize() == 0:
            print('Empty queue')
            return
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        val = self.q1.get()
        # # we need to change q1 to q2 coz all the elements are puhed to q2
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        return val

    def is_empty(self):
        pass

    def peek(self):
        pass

    def get_stack(self):
        for i in self.q1.queue:
            print(i, end=' ')
        print()


spop = Stack()
spop.push(1)
spop.push(2)
spop.push(3)
spop.get_stack()
print(spop.pop())
# spop.get_stack()


'''2. <-----making push operation costly----->'''


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.put(item)
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        # we need to change q1 to q2 coz all the elements are puhed to q2
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        if self.q2.qsize() == 0:
            print('Empty queue')
            return
        val = self.q2.get()
        print(val)

    def get_stack(self):
        for i in self.q2.queue:
            print(i, end=' ')
        print()


spush = Stack()
spush.push(4)
spush.push(5)
spush.push(6)
spush.get_stack()
spush.pop()
# spush.get_stack()


'''3. <-----stack using one queue----->'''


class Stack:
    def __init__(self):
        self.q = Queue()

    def push(self, val):
        s = self.q.qsize()
        self.q.put(val)
        for i in range(s):
            self.q.put(self.q.get())

    def pop(self):
        if self.q.empty():
            print('Empty queue')
        else:
            return self.q.get()

    def print_stack(self):
        for i in self.q.queue:
            print(i, end=' ')
        print()


s = Stack()
s.push(7)
s.push(8)
s.push(9)
s.print_stack()
print(s.pop())
# s.print_stack()


'''<-----implementation of stack using Linkedlist----->'''

# class Node:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next


# class stack:
#     def __init__(self):
#         self.head = Node(None)


'''<-----implementation of stack using deque----->'''

# stack = deque()
# stack.append('a')
# stack.append('b')
# stack.append('c')
# print(deque(stack))
# stack.pop()
# stack.pop()
# print(stack)

# print(datetime.datetime.now())
# for i in range(100000):
#     stack.append(i)
# for i in range(100000):
#     stack.pop()
# print(datetime.datetime.now())
# # 264236 ms(for list) O(n)
# # 219135 ms(for deque) O(1)
# # hence deque is a bit faster


'''<-----Implementation of Queue using stack----->'''

'''1. <-----making deQueue costly----->'''

# Unlike Stack[LIFO] Queue follows [FIFO]


class Queue:
    def __init__(self):
        # deque is bit faster than list so used deque instead of list
        self.s1 = deque()
        self.s2 = deque()

    def enQueue(self, item):
        self.s1.append(item)

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print('Queue is empty')
            return
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()

    def get_queue(self):
        print('s1:', self.s1)
        print('s2:', self.s2)


sdq = Queue()
sdq.enQueue(1)
sdq.enQueue(2)
sdq.enQueue(3)
sdq.get_queue()
print(sdq.deQueue())


'''2. <-----making enQueue costly----->'''


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, val):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def deQueue(self):
        if len(self.s1) == 0:
            print("Empty Queue")
        val = self.s1.pop()
        print(val)

    def get_queue(self):
        print('s1:', self.s1)
        print('s2:', self.s2)


seq = Queue()
seq.enQueue(4)
seq.enQueue(5)
seq.enQueue(6)
seq.get_queue()
seq.deQueue()


'''3. <-----Queue using one stack----->'''

# class Queue:
#     def __init__(self):
#         self.s = []

#     def enQueue(self, item):
#         self.s.append(item)

#     def deQueue(self):
#         pass


# q = Queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
# print(q.deQueue())
