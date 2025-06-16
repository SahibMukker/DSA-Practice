'''
basic stack implementation for practice
completed in 13 mins 20 secs, didnt know about __str__ for proper printing 
'''
class Stack:
    def __init__(self):
        self.arr = []
    
    # for proper printing of the stack, will print the acc stack (ex. [1, 2] instead of <__main__.Stack object at 0x0000020464B56A50>)
    def __str__(self):
        return str(self.arr)
        
    def push(self, val):
        self.arr.append(val)
    
    def pop(self):
        self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def isEmpty(self):
        if not self.arr:
            return True
        return False


s = Stack()

s.push(1)
s.push(2)

print(s)
print(s.isEmpty())

s.pop()
print(s.top())

s.pop()
print(s.isEmpty())