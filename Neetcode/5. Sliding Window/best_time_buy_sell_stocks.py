'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Ex 1.
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Ex 2.
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 23 mins 37secs, was doing loop wrong (some weird for loop that was wrong), i also forgot to implement l = r if prices[l] >= prices[r]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # set left and right pointers (left starts at first index, right at second)
        l, r = 0, 1
        max_profit = 0

        # run while right pointer has not reached end of prices list
        while r < len(prices):
            # if val at left pointer is smaller than val at right pointer, profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                
                # get max between curr profit and max profit
                max_profit = max(max_profit, profit)
            
            # if left pointer is not smaller than right, move left over to where
            # right pointer currently is
            else:
                l = r
            r += 1
        
        return max_profit