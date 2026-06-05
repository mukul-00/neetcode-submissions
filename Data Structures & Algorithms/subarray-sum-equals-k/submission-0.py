#=========== brute force ===============

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:

#         count = 0

#         for i in range(len(nums)):

#             sum = 0

#             for j in range(i, len(nums)):
#                 sum += nums[j]

#                 if sum == k:
#                     count += 1
        
#         return count

#=========== hash map. ==================

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0

        mp = {0: 1}

        for num in nums:

            prefix += num

            if prefix - k in mp:
                count += mp[prefix - k]

            mp[prefix] = mp.get(prefix, 0) + 1

        return count
        