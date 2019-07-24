class Stack:
    def __init__(self):
        self.list=[]

    def push(self,n):
        self.list.append(n)

    def pop(self):
        return self.list.pop()

    def display(self):
        print(self.list)

    def  isEmpty(self):
        return self.list == []
        # return list == []



stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print(stack.isEmpty())
stack.pop()
stack.pop()
stack.pop()
stack.display()

