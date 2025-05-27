'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Ex.
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Expected Time Complexity: O(n + m)
Expected Auxiliary Space: O(1)

Completed in 53 mins 26 secs
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode()
        tail = temp

        # run while both lists are not empty
        while list1 and list2:
            # if the list1 val is smaller, add it to the new list and update list1 pointer
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # updating tail pointer (regardless of whats been added)
            tail = tail.next
        
        # this is edge case of if one of the lists end before the other, add remaining to new list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # returning temp.next because the first node is a placeholder in the event both lists are empty
        return temp.next