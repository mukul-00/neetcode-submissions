class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = []
        l.extend(nums)
        l.extend(nums)
        return l