class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h =0
        for char in key:
            h = h + ord(char)
        return h % self.Max
    # For print values into hashtable
    def get(self, key):
        index = self.get_hash(key)
        temp = self.arr[index]
        while temp is not None and temp.key != key:
            temp = temp.next
        if temp is None:
            return None
        else:
            return temp.value

    # for insert values from a hashtable
    def set(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) ==2 and element [0] ==key:
                # This means the key have a element
                self.arr[h][idx] = (key,val)
                found = True
                break
            else:
                # if there is no key value then add to it.
                self.arr[h].append((key,val))

    # Function for delete a value from a hashtable
    def delete(self,key):
        h = self.get_hash(key)
        for key, element in enumerate(self.arr[h]):
            if element[0] ==key:
                del self.arr[h][key]
t = HashTable()

t.set('Thahseer',21)
t.set('Thahseer2',22)



print(t.get('Thahseer'))














