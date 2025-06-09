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

Run 2 completed in 35 mins 35 secs
took me hella long to understand why temp.next is returned and not tail.next since tail is being updated constantly
but realize that even tho tail is being updated, tail points to the LAST node in the new list, and as tail is updated,
the node is added to temp (even tho theres no explicit temp.next)
    - since tail = temp, updates to tail will also update temp and tail points to last node in temp
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

# RUN 2
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode()
        tail = temp

        # run while both lists arent empty
        while list1 and list2:
            # if list2 val is greater than list1 val, add list1 val it to the tail and update list1 pointer
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # opposite if list2 val is smaller
            else:
                tail.next = list2
                list2 = list2.next
            # updating tail regardless of whats added so in next iteration we are on next value
            tail = tail.next
        
        # this looks at if one of the lists is not empty after while loop done
        # if list1 is left, add the rest of it to the tail
        # if list2 is left, add the rest of it to the tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # returning temp.next cause temp is dummy node at start of list
        # tail is set to temp (as a pointer) and as list is built using tail.next
        # its also modifying temp (even tho temp itself isnt reassigned, the changes to tail are reflected in temp)
        return temp.next
