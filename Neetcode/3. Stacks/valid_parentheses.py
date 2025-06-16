'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 33 mins 4 secs

RUN 2:
Completed in 26 mins 19 secs, wasnt properly checking for current bracket matching open in hashmap
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        for b in s:

            # if the current character is in hashmap it is a closing bracket
            # this works cause we have all the keys in the hashmap set to the closing brackets
            if b in closeToOpen:
                # checking if stack is not empty and if top of stack matches to the
                # open bracket in hashmap
                if stack and stack[-1] == closeToOpen[b]:
                    stack.pop()
                else:
                    return False

            # if this is an open bracket keep adding to the stack
            else:
                stack.append(b)

        return True if not stack else False
    
# RUN 2:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        # iterate through string
        for i in s:
            # if current bracket is a closing bracket
            if i in closeToOpen:
                # if stack is not empty and top of stack matches associated open bracket in hashmap
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()

                # if it doesnt match, it means mismatch so return false    
                else:
                    return False

            # its an open bracket, add it to stack
            else:
                stack.append(i)
        
        # if stack empty all brackets match so return true, else false
        return True if not stack else False