'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Ex 1.
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Ex 2.
Input: nums = [7,7], k = 1
Output: [7]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 34 mins 55 secs
all my implementations werent working, had to look up neetcode solution and saw that the best way to do this
was via bucket sort and i haven't touched sorting apart from BSTs so the solution is just the neetcode copied,
gonna revist when i have learned bucket sort properly
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # this solution is bucket sort
        # i have no idea how tf that works cause i haven't touched sorting algo's yet
        # so this is the neet code solution frfr
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res