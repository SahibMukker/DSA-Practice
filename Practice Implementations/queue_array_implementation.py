'''
practice queue implementation, all time and space should be O(1) except dequeue which would be O(n)
can do linked list implementation to make it all O(1), will do this a different time

completed in 8 mins 30 secs
'''

class Queue:
    def __init__(self):
        self.q = []
        self.length = 0
    
    def enqueue(self, val):
        self.q.append(val)
        self.length += 1
    
    def dequeue(self):
        self.q.pop(0)
        self.length -=1
    
    def peek(self):
        if not self.isEmpty(): 
            return self.q[0]
        return None
    
    def size(self):
        return self.length
    
    def isEmpty(self):
        return len(self.q) == 0