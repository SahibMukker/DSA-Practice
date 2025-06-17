'''
queue implementation from scratching using linked lists, time O(1) and space O(n). 
front is front of queue and rear is back of queue, items will be added to back and removed from front 

Ex. 1 -> 2 -> 3, 1 is front and 3 is rear, want to add 4 so new LL 1 -> 2 -> 3 -> 4
Ex. 1 -> 2 -> 3 -> 4, want to remove, new LL is 2 -> 3 -> 4

Completed in 30 mins 15 secs
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, val):
        newnode = Node(val)
        
        # if its empty, new node is the front and rear (so newnode is the start of the queue)
        if self.isEmpty():
            self.front = self.rear = newnode
        
        else:
            # current rears next is now the new node instead of none, and new rear is now newnode
            self.rear.next = newnode
            self.rear = newnode
        
    def dequeue(self):
        # there is nothing that can be removed
        if self.isEmpty():
            return None
        
        # temp variable for current front that will be removed, new front is current fronts next, val variable to return temp if need that nodes data
        temp = self.front
        self.front = self.front.next
        val = temp.data
        
        if self.front == None:
            self.rear = None
        
        del temp
        return val
        
    def isEmpty(self):
        if self.front:
            return False
        
        return True
    
    def peek(self):
        if self.isEmpty():
            return None
        
        return self.front.data