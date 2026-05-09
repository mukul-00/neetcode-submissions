import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) # max in array

        while(low <= high):

            totalHours = 0

            mid = (low + high)//2

            for bananas in piles:
                totalHours += math.ceil(bananas/mid)
            
            if(totalHours <= h): #means she can eat more so we reduces the bananas/hours
                high = mid - 1
            else:
                low = mid + 1

        return low