'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Ex 1.
Input: nums = [1,2,3,2,2]

Output: 2

Ex 2.
Input: nums = [1,2,3,4,4]
Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n) try O(1)

Completed in 3 mins* (54 mins 55 secs)
so the code in here is my initial solution which took me like 3 mins which was just using hashset, iterating through and returning the dupe number
if it was in the hashset. but i treid to do the follow up trying to use constant space but couldnt figure it out.
apparently that requires fast/slow pointer or binary search, both of which i have not covered so imma come back to this after learning that
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = set()

        for n in nums:
            if n in seen:
                return n
            
            seen.add(n)