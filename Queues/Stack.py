class Stack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return print("Stack is empty")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return print("Stack is empty")
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# Pequeño ejemplo
myStack = Stack()

myStack.push('Rebanada 1')
myStack.push('Rebanada 2')
myStack.push('Rebanada 3')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack despues de hacer Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())