'''
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, 
which may point to any node in the list, or null.

Create a deep copy of the list.
The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.
Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, 
or null if it does not point to any node.

Ex.
Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 42 secs 4 secs
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        so first iterating through original list and creating copies of each node
        then mapping original node to the copy in hashmap

        then resetting curr to original head and iterating through again to assign proper
        next and random pointers for the copied nodes that are in the hashmap
        '''


        # mapping null to null to handle null pointers without extra checks
        # using this hashmap to copy original nodes and pointers so that
        # it can be used when reassigning the pointers in the copy
        oldToCopy = {None : None}

        # creating the copy nodes and storing them in hashmap without assigning pointers
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # assigning the next and random pointers using the original copy in the hashmap
        curr = head
        while curr:
            # get copy of current node that is in the hasmap
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

            curr = curr.next

        # returning copied list starting from the first node
        return oldToCopy[head]

