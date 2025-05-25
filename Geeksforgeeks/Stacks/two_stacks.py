'''
Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.
twoStacks : Initialize the data structures and variables to be used to implement  2 stacks in one array.
push1 : pushes element into the first stack.
push2 : pushes element into the second stack.
pop1 : pops an element from the first stack and returns the popped element. If the first stack is empty, it should return -1.
pop2 : pops an element from the second stack and returns the popped element. If the second stack is empty, it should return -1.

Ex.
Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
Output: [3, 4, -1]
Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence returned -1.

Constraints:
1 <= number of queries <= 104
1 <= number of elements in the stack <= 100
The sum of the count of elements in both the stacks < size of the given array

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Completed in 47 mins 36 secs
'''
class TwoStacks:
    def __init__(self):
        # constraint of question is 100 so making array of size 100
        self.size = 100
        self.a = [0]*self.size
        
        # logic is that one list is gonna be left to right, other right to left
        self.top1 = -1
        self.top2 = self.size
    
    # Function to push an integer into stack 1
    def push1(self, x):
        
        # checking to make sure the two dont run into each other
        # so if next index is free, add to the stack
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.a[self.top1] = x
        else:
            pass

    # Function to push an integer into stack 2
    def push2(self, x):
        if self.top1 + 1 < self.top2:
            # since going right to left, -= 1 instead of += 1
            self.top2 -= 1
            self.a[self.top2] = x
        else:
            pass

    # Function to remove an element from top of stack 1
    def pop1(self):
        
        # checks if stack is empty
        if self.top1 < 0:
            return -1
        else:
            # returning "removed" value and moving top pointer down
            popped = self.a[self.top1]
            self.top1 -= 1
            return popped
    
    # Function to remove an element from top of stack 2
    def pop2(self):
        
        # checks if stack is empty
        if self.top2 == self.size:
            return -1
        else:
            # returning "removed" value and moving top pointer up in this case
            popped = self.a[self.top2]
            self.top2 += 1
            return popped