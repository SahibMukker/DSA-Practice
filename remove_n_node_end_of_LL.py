'''
You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.

Ex.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 25 mins 14 secs, was messing up my while loop to get right pointer to be n spaces away
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # setting dummy to have value 0 and the next pointer is head
        dummy = ListNode(0,head)

        left = dummy
        # to get proper right pointer, set it to head and run while n > 0 and right isnt null
        # keep shifting right pointer to right and decrement n by 1
        # when loop is done, right pointer will be n spaces away from left pointer
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # shifting pointers till right is null (at this point lefts next is pointer to be deleted)
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        # returning dummy.next since we dont want to include dummy itself
        return dummy.next

