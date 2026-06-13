class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            
            # when mid, low and high elements are same
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                
            # right half sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                
        return False