class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        newList = []

        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if i != j:
                    mult *= nums[j]
            newList.append(mult)
        return newList