'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. 
The tail node of the list will set it's next pointer to the index-th node.
If index = -1, then the tail node points to null and no cycle exists.
Note: index is not given to you as a parameter

Ex. 
1 -> 2 -> 3 -> 4
     ^---------|
Input: head = [1,2,3,4], index = 1
Output: true

Ex 2.
Input: head = [1,2], index = -1
Output: false

28 mins 17 secs
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using hashmap to keep track of the nodes that have been visited
        seenHash = {""}
        curr = head

        # keep iterating through the entire linked list
        # if the current node is in the hashmap, return true
        # if it isnt, add it into the hashmap and update the pointer to move forward
        while curr:
            if curr in seenHash:
                return True
            else:
                seenHash.add(curr)
                curr = curr.next
        return False