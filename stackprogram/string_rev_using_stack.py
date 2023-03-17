class Stack_to_reverse:
    def __init__(self):
        self.items = list()
        self.size = -1
    def isEmpty(self):
        if (self.size == -1):
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size -= 1
    def push(self, item):
        self.items.append(item)
        self.size += 1
    def reverse(self, string):
        n = len(string)
        # Push all characters of string to stack
        for i in range(0, n):
            S.push(string[i])
        # Making the string empty since all characters are saved in stack
        string = ""
        # Pop all characters of string and put them back to string
        for i in range(0, n):
            string += S.pop()
        return string
S = Stack_to_reverse()
seq = input("Enter a string to be reversed")
sequence = S.reverse(seq)
print("Reversed string is " + sequence)