class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def delete_node(self, head, x):
        
        curr = head
        # traversing to end of list
        # breaking out of loop is curr dont exist
        for i in range (1, x):
            if curr is None:
                break
            
            curr = curr.next
            
        # updating next nodes previous pointer    
        if curr.next is not None:
            curr.next.prev = curr.prev
        
        # updating previous nodes next pointer
        if curr.prev is not None:
            curr.prev.next = curr.next
            
        # if the node to be deleted is the head node
        if head == curr:
            head = curr.next
            
        # deleting and returning the list
        del curr
        return head