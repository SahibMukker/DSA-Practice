'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Ex 1.
Input: n = 1
Output: ["()"]
Ex 2.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.

Constraints:
1 <= n <= 7

Expected Time Complexity: O(4^n / sqrt(n))
Expected Auxiliary Space: O(n)

Completed in 59 mins 23 secs, kinda knew that a stack was needed to hold parens
and knew logic of how to keep track of open and closed parens, but have no idea how to properly implement
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # gonna be final list of all the parentheses
        result = []
        # gonna hold parens
        stack = []
        # two variables keeping track of number of close and open parentheses
        # they should both only be able to be n (can only have n open/close paren)
        # also can only add a new paren if there open > closed and if open < n
        
        def backtrack(openP, closedP):
            if openP == closedP == n:
                # join every character in the stack and join them tg into empty string
                result.append(''.join(stack))
                return
            
            # checking if we are allowed to add more parentheses
            if openP < n:
                stack.append('(')
                # recursively continue and increment open by 1 since we just added a new parenthese
                backtrack(openP + 1, closedP)
                # have to update stack by popping so that algo can go back and try other option to
                # see if its valid
                # ex. lets say ['(', '('], algo will add another open so stack = ['(', '(', '(']
                # but now you go back to see if you can add ')' and keep doing that till all valid
                # combos have been added to result
                stack.pop()
            
            # have to make sure that number of open paren is greater than closed otherwise invald
            # ex. n = 3 and stack = (()means can add closed but (()) = invalid since open == closed
            if openP > closedP:
                stack.append(')')
                backtrack(openP, closedP + 1)
                stack.pop()
            '''
            ex. n = 2
            start -> "" (open=0, close=0)
                -> "(" (open=1, close=0)
                    -> "((" (open=2, close=0)
                        -> '(' invalid (can't add "(" anymore, and open > close)
                        -> "(())" ✔
                -> "(()" (open=2, close=1)
                    -> '(' invalid (can't add "(" anymore since open = n)
                -> "()" (open=1, close=1)
                    -> "()(" -> "()()" ✔

            '''

        # openP and closedP both start at 0 since no parens have been added yet
        backtrack(0,0)
        return result