'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Ex.
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 8 mins 57 secs
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev is gonna be new head
        curr = head
        prev = None

        while curr:
            # temp variable for the next node
            next_node = curr.next
            # make the next pointer point to the previous node and update previous
            # to be the node we're currently on
            curr.next = prev
            prev = curr
            # update curr to next node for next iteration
            curr = next_node
        
        return prev