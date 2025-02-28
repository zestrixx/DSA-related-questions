import sys
sys.stdin = open('D:\\Coding Env\\4. PYTHON\\input.txt', 'r')
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_(self):
        if self.head is None:
            print('Empty LinkedList')
            return
        ptr = self.head
        llstr = ""
        while ptr:
            llstr = llstr + str(ptr.data) + "->"
            ptr = ptr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(data, None)

    def reversed_list_iterative(self):
        if self.head is None:
            return 'll is empty'
        tmp = None
        ptr = self.head
        while ptr:
            nxt = ptr.next
            ptr.next = tmp
            tmp = ptr
            ptr = nxt
        self.head = tmp
 
    def reversed_list_recursive(self):
        def reversed_list_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return reversed_list_recursive(cur, prev)
        self.head = reversed_list_recursive(cur=self.head, prev=None)

    def del_duplicate_sorted(self):  # in sorted list
        if self.head is None:
            return
        ptr = self.head
        while ptr.next:
            if ptr.data == ptr.next.data:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return self.head

    def del_duplicate_unsorted(self):  # in unsorted list
        if self.head is None or self.head.next is None:
            return self.head
        ptr = self.head
        hash = set()
        hash.add(self.head.data)
        while ptr.next:
            if ptr.next.data in hash:
                ptr.next = ptr.next.next
            else:
                hash.add(ptr.next.data)
                ptr = ptr.next
        return self.head
    
    def find_middle(self):
        if not self.head:
            return None
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def merge_list(self, ll2):
        p1 = self.head
        p2 = ll2.head
        if not p1:
            return p2
        if not p2:
            return p1
        if p1 and p2:
            while p1.next:
                p1 = p1.next
            p1.next = p2
        return p1

    def merge_list_sort(self, ll2):
        p1 = self.head
        p2 = ll2.head
        s = None
        if not p1:
            return p2
        if not p2:
            return p1
        if p1 and p2:
            if p1.data <= p2.data:
                s = p1
                p1 = s.next
            else:
                s = p2
                p2 = s.next
            new_head = s
        while p1 and p2:
            if p1.data <= p2.data:
                s.next = p1
                s = p1
                p1 = p1.next
            else:
                s.next = p2
                s = p2
                p2 = p2.next

        if not p1:
            s.next = p2
        if not p2:
            s.next = p1
        return new_head

    def insert_in_sorted(self, val):
        if not self.head:
            return -1
        if not self.head.next:
            if self.head.data<val:
                self.head.next = Node(val, None)
            nd = Node(val, self.head)
            self.head = nd
            return self.head
        ptr1 = self.head
        while ptr1.next:
            if ptr1.data<val<ptr1.next.data:
                nd = Node(val, ptr1.next)
                ptr1.next = nd
            ptr1 = ptr1.next
        return self.head
    
    def delete_node(self, key):
        if not self.head:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def reverse_linkedlist(self):
        if not self.head:
            return
        if not self.head.next:
            return self.head
        prev = None 
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def count_occ(self, data):
        ptr = self.head
        count = 0
        while ptr:
            if ptr.data == data:
                count += 1
            ptr = ptr.next
        return count


ll = LinkedList()
ll2 = LinkedList()

ll.insert_at_beginning(2)
ll.insert_at_end(3)
ll.insert_at_end(7)
ll.insert_at_end(10)
ll.insert_at_end(40)

ll2.insert_at_beginning(4)
ll2.insert_at_end(6)
ll2.insert_at_end(1)
# ll.merge_list_sort(ll2)
# ll.del_duplicate_sorted()
# ll.del_duplicate_unsorted()
ll.print_()
# ll.reversed_list_iterative()
# ll.print_()
# ll.reversed_list_recursive()
# ll.insert_in_sorted(5)
ll.reverse_linkedlist()
ll.print_()
# ll2.print_()
# print(ll.count_occ(20))

# ll.merge_list_sort(ll2)
# ll.print_()
# print(ll.find_middle())
