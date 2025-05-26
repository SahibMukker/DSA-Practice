'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Ex.
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 42 mins 10 secs
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to keep track of current result
        # will do each operation and add it to the stack and return top of stack at end
        stack = []
        for t in tokens:
            
            # pop the previous two values and add them
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            
            # pop the previous two values and subtract them
            elif t == '-':
                # pop the two and subtract second from first
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)

            # pop the two values and multiply them
            elif t == '*':
                stack.append(stack.pop() * stack.pop())

            # pop the two values and divide second by the first and append that value to the stack
            elif t == '/':
                num1, num2 = stack.pop(), stack.pop()
                # surrounding the operation with int rounds towards 0
                # my original implementation of stack.append(num2 // num1) was wrong cause that
                # rounds DOWN not TOWARDS 0
                stack.append(int(num2 / num1))
            
            # if no operation, turn the string to int and add it to the stack
            else:
                stack.append(int(t))

        # return beginning of stack since everything but the final answer should remain in stack
        return stack[0]