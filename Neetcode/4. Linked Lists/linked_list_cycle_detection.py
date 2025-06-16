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

Run 2:
Completed in 15 mins 4 secs, pre easy i spent most time making sure if i had the correct code cause i thought theres no way i got this in
4 mins
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using hashmap to keep track of the nodes that have been visited
        # NOTE: this is a hashSET (another way to make hash set is to use set())
        # using set because we only need to check if a value is in there, not where it is
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

# RUN 2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using hashset to keep track of nodes already seen
        seen = set()
        curr = head

        # while curr, check if curr in seen, if it is then there is a cycle
        while curr:
            if curr in seen:
                return True

            # if not in hashset, add to seen since now its been seen and update next pointer
            seen.add(curr)
            curr = curr.next

        # default false since if it dont return true in the while loop, that means
        # there is no cycle
        return False