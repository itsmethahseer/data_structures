class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            temp = self.table[index]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(key, value)


    def get(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp is not None and temp.key != key:
            temp = temp.next
        if temp is None:
            return None
        else:
            return temp.value

t = HashTable(20)
t.add(10,"helo")
# print(t.get(10))
