'''
You are given a string s , the task is to reverse the string using stack.

Ex.:
Input: s ="GeeksforGeeks"
Output:  skeeGrofskee

Constraints:
1 ≤ s.length() ≤ 100

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Took me 11 mins 59 secs
'''
class Solution:
    def reverse(self, s: str) -> str:
        stack = []
        
        # iterating through string and adding each letter to the stack
        for l in s:
            stack.append(l)
        
        reversed_stack = ""
        
        # while going through the stack, remove the last letter and add it to the reversed stack
        while stack:
            reversed_stack += stack.pop()
            
        return reversed_stack