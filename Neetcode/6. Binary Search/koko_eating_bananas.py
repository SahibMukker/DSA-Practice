'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.

Ex 1.
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. 
With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Ex 2.
Input: piles = [25,10,23,4], h = 4
Output: 25

Expected Time Complexity: O(nlogm), where n = len(piles) and m = max(piles)
Expected Auxiliary Space: O(1)

Completed in 45 mins 28 secs, had rough idea but i didnt know how to efficiently get max of list 
(thought the only way was to sort so that made time complexity bigger) and then i had l = 0 and r = len(piles) which is wrong

Run 2:
competed in 27 mins 57 secs, originally was iterating through each string and then binary search in that, which is wrong
then i realized i need to do binary search and then iterate through array to get total time
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # pointers are from lowest eating rate (1 banana/hr) to max/hr
        # ex. [1,2,3,4,5], l = 1 and r = 5 so default result = r
        # and binary search being used to find the min k
        l = 1
        r = max(piles)

        result = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            # calculating time taken for current k (mid) and adding all piles vals
            # if the total time is less than hours, res is current k
            # and then move right pointer down (r = k - 1) and check again
            
            for b in piles:
                # add current time taken to hours
                hours += math.ceil(b / k)

            # if current hours is <= h, update to new minimum result and move right pointer else left
            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
            
        return result
    
# Run 2: July 3rd 2025
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo, hi = 1, max(piles)
        result = hi

        while lo <= hi:
            k = (lo + hi) // 2

            # getting time taken for current k
            time = 0
            for i in piles:
                time += math.ceil(float(i) / k)
            
            # if time <= h, update result and search left
            if time <= h:
                result = k
                hi = k - 1
                
            # else search right
            else:
                lo = k + 1
        
        return result