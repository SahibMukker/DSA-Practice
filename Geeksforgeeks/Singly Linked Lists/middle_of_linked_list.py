'''
Given the head of a linked list, the task is to find the middle. 
For example, the middle of 1-> 2->3->4->5 is 3. 

If there are two middle nodes (even count), return the second middle. 
For example, middle of 1->2->3->4->5->6 is 4.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Took me 13 mins 25 secs
'''

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        LL_length = self.getLength(head)
        
        # get mid point (floor cause cant have half mid type beat)
        mid = LL_length // 2
        
        #traverse till we reach mid point and return the mid node
        while mid:
            head = head.next
            mid -= 1
            
        return head.data
    
    # traverses through LL and counts number of nodes    
    def getLength(self, head):
        counter = 0
        
        while head:
            counter += 1
            head = head.next
            
        return counter