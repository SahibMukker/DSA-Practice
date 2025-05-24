'''
Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.
Ex.
Input: Linked List: 1->2->1->2->1->3->1, key = 1
Output: 4

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ number of nodes, key ≤ 10^5
1 ≤ data of node ≤ 10^5

Took me 3 mins 33 secs
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
class Solution:
    def count(self, head, key):
        
        # initializing counter and traversing through linked list
        counter = 0
        while head:
            # whenever the node matches the key, add one to the counter and move to the next node
            # return the counter when done
            if head.data == key:
                counter += 1
                
            head = head.next
                
        return counter