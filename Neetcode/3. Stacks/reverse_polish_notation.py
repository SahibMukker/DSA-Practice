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

RUN 2:
Completed in 31 mins 33 secs, was ab to give up early and look at solution but i forced myself to draw out solution and figured it out
only thing messing me up was forgetting to set num1 and num2 for - and / operations, and also forgetting to use int() to round towards 0 for /
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

# RUN 2: June 24th 2025
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):

            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif tokens[i] == '-':
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                stack.append(num2 - num1)
            
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            
            elif tokens[i] == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                # this rounds towards 0
                stack.append(int(num2 / num1))

            # if not an operator, add the num onto stack as int
            else:
                stack.append(int(tokens[i]))
        # return beginning of stack cause need to return int not list, and first element is answer
        return stack[0]

        