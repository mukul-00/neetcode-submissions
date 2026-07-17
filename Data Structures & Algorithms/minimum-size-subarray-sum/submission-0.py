class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = 0
        min_len = float("inf")
        curr_sum = 0

        for j in range(len(nums)):

            curr_sum += nums[j]

            while curr_sum >= target:

                min_len = min(min_len, j - i + 1)

                curr_sum -= nums[i]

                i += 1
        
        if min_len == float("inf"):
            return 0
        
        return min_len


