'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

Expected Time Complexity: O(1) for all operations
Expected Auxiliary Space: O(n) for all operations

Completed in 25 mins 14 secs, figuring out storing min val and updating it properly was hardest part for me
'''
class MinStack:
    # initializing min stack with two stacks (a stack to keep track of all added values, and another that keeps track of the min value)
    def __init__(self):
        self.stack = []
        self.minval = []

    # add the value to the stack
    # if minval is not empty, make temp variable that will get the min between current value that is being added and current top of minval(so current min value)
    # if min val is empty, then the current min is the value being added
    # append the minval to the minval stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        # ex. we adding 3, 2, 4
        # stack = [3, 2, 4]
        # minval = [3, 2, 2] since min val between 4 and current minval (2) is 2
        if self.minval:
            curr_min = min(val, self.minval[-1])
        else:
            curr_min = val

        self.minval.append(curr_min)

    # remove the top value from both stacks
    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()

    # return top of the stack
    def top(self) -> int:
        return self.stack[-1]

    # return top of minval stack (which is the min value)
    def getMin(self) -> int:
        return self.minval[-1]