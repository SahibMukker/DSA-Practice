'''
Given a singly linked list, your task is to remove every kth node from the linked list.
Ex.
Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
Output: 1 -> 3 -> 5 -> 7


Expected Time Complexity:  O(n)
Expected Auxiliary Space:  O(1)


Took me 30 mins 4 secs, 3 submissions
'''


class node():
    def __init__(self, data):
        self.data = data
        self.next = None




def deleteK(self, head, k):
    # if counter set to 0, k+1th node will be removed not kth node
    counter = 1
    # temp pointer to traverse linked list
    temp = head
    '''
    counter is 1 ahead of temp. when counter is divisible by k,
    that means that the next node needs to be removed (since counter is ahead by 1).
    thats why we set temp.next to temp.next.next
    so lets say LL is 1,2,3,4,5 and k is 3,
    this will traverse till 2, set the next to be 4 and carry forward
'''
       
    # running till temp.next is not none cause wanna stop before the node that we might delete
    while temp.next is not None:
        counter += 1
           
        if counter % k == 0:
            temp.next = temp.next.next
        else:
            temp = temp.next
               
    return head