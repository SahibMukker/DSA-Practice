'''
You are given the head of a singly linked list. Your task is to determine if the linked list contains a loop. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

Custom Input format:
A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

Ex.

Input: head: 1 -> 3 -> 4, pos = 2
            1 -> 3 -> 4
                 ^----|
Output: true
Explanation: There exists a loop as last node is connected back to the second node.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Completed in 13 mins 12 secs, had all the logic down but only thing 
i messed up was adding curr to the hashset before checking if it was in the hashset
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        
        # using set to keep track of nodes already seen
        curr = head
        check = set()
        
        # while the linked list exists, if the current node is in the hashset, return true
        # other wise add the current node to the hashset to show its been seen and then move on to next node
        while curr:
            if curr in check:
                return True
            
            check.add(curr)
            curr = curr.next
        
        return False