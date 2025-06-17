'''
stack implementation from scratch using LLs, everything should be O(1) time, head of the list is top of stack so when adding, we adding before head.
Ex: 1 -> 2 -> 3 and want to insert 4 to stack, new LL is 4 -> 1 -> 2 -> 3
When removing, head is removed since LIFO
Ex: 1 -> 2 -> 3 and want to remove, new LL is 2 -> 3

Completed in 18 mins 1 sec
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        newnode = Node(val)
        
        # make new node point to current head and then make the new node the head
        newnode.next = self.head
        self.head = newnode        
        
    def pop(self):
        
        if self.isEmpty():
            print('stack underflow')
            return None
        
        # store curr head in temp variable, set head to be the next node, delete temp
        temp = self.head
        self.head = self.head.next
        val = temp
        del temp
        
        return val
            
    def isEmpty(self):
        if not self.head:
            return True
        return False
    
    def top(self):
        # if LL is empty, return statement, else return the curr heads value
        if self.isEmpty():
            return None
        
        return self.head.data