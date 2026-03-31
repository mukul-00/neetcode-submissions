class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            target = -nums[i]

            while(j < k):
                if(nums[j] + nums[k] == target):
                    l.append([ nums[i], nums[j], nums[k]] )
                    j = j + 1
                    k = k - 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif (nums[j] + nums[k] < target):
                    j = j + 1
                
                else:
                    k = k - 1
        return l