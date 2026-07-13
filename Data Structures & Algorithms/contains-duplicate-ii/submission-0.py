class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        i = 0
        freq = {}

        for j in range(len(nums)):

            freq[nums[j]] = freq.get(nums[j], 0) + 1

            if freq[nums[j]] > 1:
                return True

            if j - i + 1 > k :

                freq[nums[i]] -= 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]

                i += 1
        
        return False
