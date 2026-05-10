from typing import List

class Solution:
    
    def findDays(self, weights, capacity):
        
        days = 1
        load = 0
        
        for weight in weights:
            
            # move to next day
            if load + weight > capacity:
                days += 1
                load = weight
            else:
                load += weight
                
        return days

    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            
            mid = (low + high) // 2
            
            requiredDays = self.findDays(weights, mid)
            
            if requiredDays <= days:
                high = mid - 1
            else:
                low = mid + 1
                
        return low