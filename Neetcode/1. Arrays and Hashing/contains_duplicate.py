'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
Ex. 
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 2 mins 56 secs
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using set because we can check if a value is in there
        result = set()

        # goes through list, if there is a duplicate return true, if not then add that number
        # to the result set and keep iterating through the list
        for n in nums:
            if n in result:
                return True
            result.add(n)
        return False