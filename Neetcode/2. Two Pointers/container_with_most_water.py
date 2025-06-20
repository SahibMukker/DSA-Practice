'''
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 20 mins 10 secs, was a bit confused but had right approach, i started watching neetcode solution and while he was explaining question i figured it out
before he got to the logic
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            # get current area, r-l is width and getting min height of l and r since water cant go above smallest height or else overflows
            area = (r-l) * min(heights[l], heights[r])
            result = max(result, area)

            if heights[r] > heights[l]:
                l += 1
            
            elif heights[r] < heights[l]:
                r -= 1
            
            else:
                # can either increment left or decrement right, does same thing
                # since this else is same as above elif, can get rid of elif but
                # imma keep in this run for future me
                r -= 1

        return result
