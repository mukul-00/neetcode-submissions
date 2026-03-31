class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # BRUTE FORCE

        # maxWater = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         maxWater = max(maxWater, area)
        # return maxWater

        maxWater = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            width = r - l
            height = min(heights[r], heights[l])
            area = width * height
            maxWater = max(maxWater, area)

            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return maxWater