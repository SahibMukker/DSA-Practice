'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Ex.
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 15 mins 38 secs, surprised i acc knew what to do
originally i had a diff variable checking for the difference between the target and the current number and if the diff was > 0, move right pointer down else move
left pointer up and if nums[l] + nums[r] == target, return [l+1, r+1] but that was wrong so i reevaluated and realized its better to check current sum from the start
and move the pointers according to target and that gave me right answer
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            # get current sum, if its greater than target move right pointer down
            # if its smaller than targer move left pointer up
            # else we have solution
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            
            else:
                return [l+1, r+1]