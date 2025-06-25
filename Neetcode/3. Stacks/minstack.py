'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Ex.
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Completed in 30 mins 57 secs

RUN 2: 
Completed in 17 mins 20 secs, was not properly pushing on minstack(no if check to see if minstack is empty)
'''
class MinStack:

    def __init__(self):
        # using two stacks, one for keeping track of values and another for tracking min val
        self.stack = []
        self.minval = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if minval has values, compare current val and top of minval stack and set curr to the min between the two
        # if minval is empty, set current min to be the val that was just appended
        
        if self.minval:
            curr_min = min(val, self.minval[-1])
        else:
            curr_min = val

        self.minval.append(curr_min)

    def pop(self) -> None:
        # have to pop both since im updating both stacks for what the current val and minval is
        self.stack.pop()
        self.minval.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]
    
# RUN 2: June 24th 2025
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minstack:
            curr_min = min(self.minstack[-1], val)
        else:
            curr_min = val

        self.minstack.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
