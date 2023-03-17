class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]


    def get_hash(self,key):
        h =0
        for char in key:
            h = h+ ord(char)
        return h % self.Max

    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] =val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]


    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None





t = HashTable()
print(t.get_hash('march 6'))
# calling adding methode for add value into a dictionary
t.add('March 6',130)
# print before deleting the value
print(t.get('March 6'))

t.delete('March 6')
# print after deleting the value
print(t.get('March 6'))



