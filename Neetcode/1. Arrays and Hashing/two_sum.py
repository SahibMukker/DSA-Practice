'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Ex.
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 13 mins 34 secs
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash since we can map value to index and check if a value exists in it
        hashmap = {}
        
        # iterating through list, this is code to get index and value
        for i, n in enumerate(nums):
            # diff is the number we need to reach target
            diff = target - n
            
            # if diff exists in the hashmap, return its index and the index of n
            if diff in hashmap:
                return [hashmap[diff], i]

            # adding iteration to the hashmap
            hashmap[n] = i