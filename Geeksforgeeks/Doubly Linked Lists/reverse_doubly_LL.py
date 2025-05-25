'''
Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.
Ex.
Input: LinkedList: 3 <-> 4 <-> 5
Output: 5 <-> 4 <-> 3

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Completed in 17 mins 23 secs
'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        curr = head
        prev = None
        
        while curr:
            # storing next node
            next_node = curr.next
            
            # reversing the next and prev pointers
            curr.next = prev
            curr.prev = next_node
            
            # new prev is now the node currently on, new curr is the next node stored early
            prev = curr
            curr = next_node
            
        return prev