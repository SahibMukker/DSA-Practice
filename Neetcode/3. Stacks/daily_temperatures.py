'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Ex.
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 55 mins 9 secs, figuring out the while loop 
and how to use keep track of days + temps is what gave me most trouble

RUN 2:
Completed in 30 mins 43 secs

Run 3:
Completed in 34 mins 14 secs, couldnt figure why/where to implement stack, messed up inner for loop
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result stack is gonna be as long as there are number of temperatures, default 0
        # since if there is no higher temp, the default value will be 0
        result = [0] * len(temperatures)
        
        # using a stack to keep track of how many days till next higher temps
        # contains pair: [temp, index]
        # making stack in decreasing order (top is most recent unresolved temp, and then)
        # can work back and figure out number of days between current and previous temps
        stack = []

        for i, t in enumerate(temperatures):

            # this loop compares current temp with top of stack and if top of stack
            # is smaller (colder day), you remove it and compute the days between
            # and then keep checking for any more colder days before appending more stuff in the stack
            while stack and t > stack[-1][0]:
                
                # setting stack temp and index is the value we are removing
                # so it is the past day that is waiting for warmer day, i is current day
                stackTemp, stackIndex = stack.pop()
                
                # updating past day to reflect how many days it took for warmer day to come
                result[stackIndex] = (i - stackIndex)

            # append the temp and index of the temp we are currently on
            stack.append([t,i])
        
        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # res array will be size of temps with default values 0 so end is easier to worry about
        res = [0]* len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # if stack not empty and current temp (t) greater than temp at top of stack
            # get the temp and index, update days between t and top of stack
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            # add current temp and its index to top of stack
            stack.append((t,i))
        
        return res
    
# RUN 3: July 1st 2025
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = [] # stack tracking tuple of temp, index

        # iterate through temps and get index and temp
        for i, t in enumerate(temperatures):
            # while stack not empty and current temp greater than temp at top of stack
            while stack and t > stack[-1][0]:
                # pop and store index, update result array at index to diff between curr and next hottest
                temp, index = stack.pop()
                result[index] = i - index
            
            # adding current temp and index to stack
            stack.append((t, i))

        return result