class stackArray:
    def _init_(self):
        self.stack = [None] * 5
        self.top = -1

    def push(self, data):
        self.top = self.top + 1
        self.stack[self.top] = data

    def pop(self):
        # self.stack[self.top]=0
        self.top = self.top - 1

    def display(self):
        if self.top == -1:
            print("stack underflow")
            return
        temp = self.top
        for i in range(temp + 1):
            print(self.stack[i])


stack = stackArray()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.display()
print("-------")
stack.pop()
stack.push(60)
stack.display()