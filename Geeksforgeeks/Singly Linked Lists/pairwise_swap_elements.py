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
        # if LL is empty or has only one node, no swap needed
        if not head or not head.next:
            return head

        # curr is traversal pointer
        curr = head
        # after first swap, second node becomes new head
        new_head = head.next
        # prev keeps track of last node in the previous pair
        prev = None

        # loop while there are at least two nodes to swap
        while curr and curr.next:
            # store the current pair to be swapped
            first = curr
            second = curr.next
            # move curr ahead by 2 for next pair
            curr = curr.next.next

            # if this is not the first pair, connect the last node of previous pair to current second
            if prev:
                prev.next = second

            # swap the pair
            second.next = first
            first.next = curr

            # prev becomes the last node of the current pair for next loop
            prev = first

        # return the new head (was the second node in the original list)
        return new_head