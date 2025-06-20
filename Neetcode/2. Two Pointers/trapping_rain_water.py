'''
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Ex.
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Expected time complexity: O(n)
Expected auxiliary space: O(1)

Completed in 50 mins 22 secs, had kind of an idea but it was mostly similar to container with most water problem, had to look at solution
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        
        # edge case if rempty input
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        result = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                
                # since updating left max above, there will never be a negative
                result += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result
            