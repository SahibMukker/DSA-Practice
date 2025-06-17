'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Return the sum of the two numbers as a linked list.

Ex 1.
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]
Explanation: 321 + 654 = 975.

Ex 2.
Input: l1 = [9], l2 = [9]
Output: [8,1]

Completed in 45 mins 26 secs, my original implementation was using like 3 stacks and 3 while loops popping adding to string and then inting it but that solution
was hella slow and i also couldnt fully figure it out, watched neetcode solution and before he finished explaining i figured out most of what to do except
how to get the carry over to the next digit, val mod 10, and wasnt checking while carry nonzero
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        carry = 0

        # keep looping if l1 or l2 or carry or not null
        # while carry: is same as while carry != 0, need to do this for edge case
        # of ex. 7 + 8, 5 need to carry over 1 to give 15, but if we dont check
        # for nonzero carry, the 1 will be missed and the LL will have 5 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry

            # get carry out of it by flooring by 10 and get rear by mod 10
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)

            # updating pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next