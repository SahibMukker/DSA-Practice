'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Ex.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Expected Time Complexity: O(n^2)
Expected Auxiliary Space: O(n)

Completed in 32 mins 19 secs, had to look at solution
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # go through all nums as potential first num
        for i, a in enumerate(nums):
            if a > 0:
                break
            # want to skip duplicate nums
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = a + nums[l] + nums[r]
                
                # if curr sum too big, make it smaller by moving right pointer down
                # else move left pointer up
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    # update pointers
                    # ex. at [-2, -2, 0, 0, 2, 2]
                    #          L               R
                    # only need to shift 1 pointer, other pointer taken care of up top
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return result