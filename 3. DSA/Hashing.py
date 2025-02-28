import sys
sys.stdin = open('D:\\Coding Env\\4. PYTHON\\input.txt', 'r')
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')

'''dictionary is the specific implementaion of hashmap in python, we have map/unordered_map in c++ as hashtable/hashmap/dictionary'''

'''we have to def hash function to implement hashtable/hashmap'''

'''different hashing methods
    1. Chaining --> appending in a list or linklist
    2. Open addressing --> i)linear probing
                          ii)quadratic probing
                         iii)double hashing
'''

# def hash(key):
#     h = 0
#     for ch in key:
#         h += ord(ch)
#     return h % 100  # (100 is the size of list)

# lets check what is the hash of a 'string key'


# print(hash('march 22'))

''' m-->109
    a-->97
    r-->114
    c-->99
    h-->104
    '(space)'-->32
    22-->SYN

    total-->555
    555%100-->55(result)
    (modulo value will always lie btw 0 and len(arr)-1 )
'''


class Hashtable:
    def __init__(self):
        self.max = 10
        self.__array = [[] for _ in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # avoiding collision case
        found = False
        for idx, element in enumerate(self.__array[h]):
            if len(element) == 2 and element[0] == key:
                self.__array[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.__array[h].append((key, value))

    # used __getitem__ to use the functionality of accessing value like in a dict (d['key']) so that we don't need to use dic.get('key'){where get is the function} instead we use dic['key']
    def __getitem__(self, key):
        h = self.get_hash(key)
        # iterating through each tuples to get the value of given key
        for element in self.__array[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.__array[h]):
            if element[0] == key:
                del self.__array[h][idx]

    def get_array(self):
        return self.__array


dic = Hashtable()
dic['march 6'] = 6
dic['abhi'] = 62
dic['march 17'] = 17
print(dic['march 6'])
print(dic['abhi'])
del dic['march 6']
print(dic.get_array())
