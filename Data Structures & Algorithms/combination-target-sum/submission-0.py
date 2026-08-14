class Solution:

    def combSum(self, arr, i , ans, comb, target):
        if target == 0:
            ans.append(comb[:])
            return 
        
        if i == len(arr) or target < 0:
            return

        # add current element
        comb.append(arr[i])

        self.combSum(arr, i, ans, comb, target - arr[i])

        comb.pop()

        self.combSum(arr, i + 1, ans, comb, target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        self.combSum(nums, 0, ans, [], target)
        return ans
        