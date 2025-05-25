'''
Given a singly linked list. The task is to swap elements in the linked list pairwise. 
For example
Input: LinkedList: 1->2->2->4->5->6->7->8
Output: 2->1->4->2->6->5->8->7

Took me 40 mins 36 secs and i still have no idea on wtf is going on gonna need to revisit this fr
'''

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        
        curr = head
        # new head of list after first swap
        new_head = head.next
        prev = None
        
        while curr and curr.next:
            # store nodes for swap
            first = curr.next
            second = curr
            
            # move to next pair
            curr = curr.next.next
            
            # if past the first pair, connect  previous pair to current pair's new first node (second).
            if prev:
                prev.next = second
            
            #swap pair
            second.next = first
            first.next = curr
            
            # prev updated for next iteration 
            prev = first
        
        return new_head