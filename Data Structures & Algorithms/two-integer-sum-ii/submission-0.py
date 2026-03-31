class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l , r = 0, len(nums) - 1

        while l < r:
            guess = nums[l] + nums[r]
            if(guess == target):
                return [l+1, r+1]

            if(guess > target):
                r = r - 1
            else:
                l = l + 1




