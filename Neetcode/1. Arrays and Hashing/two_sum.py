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

Completed in 18 mins 12 secs, understand the logic a lot more this time now that ive formally learned about hashmaps,
it took me like 5 mins to code it because ive done twosum so much, the rest of the time was spent figuring out
why hashmap[n] = i and not hashmap[i] = n (figured out that hashmap[i] = n is wrong because indices are being stored as values, not keys)

Run 3:
Comopleted in 17 mnins 40 secs, was checking if n in hashmap instrad of diff in hashmap, wasnt doing question properly (tried to remember solution instead of work it out)
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
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap to map val : index
        hashmap = {}

        # run through the list to get current index and value at that index
        for i, n in enumerate(nums):
            # since all inputs have a solution, target = current(n) - some val
            # therfore some val's index is the diff between the target and n
            diff = target - n
            # check if this val is in the hashmap, if it is then return the indices
            # hashmap[diff] is the number we are looking for in the hashmap,
            # i gives the index of the number that the loop is currently at
            #   - (the number that was used to calculate diff)
            if diff in hashmap:
                return [hashmap[diff], i]
            
            # if diff is not in hashmap, then add it to the hashmap
            hashmap[n] = i

# RUN 3: July 1st 2025
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mapping num : index
        hashmap = {}

        for i, n in enumerate (nums):
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i