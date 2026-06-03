class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # result = []

        # for num in nums:

        #     count = 0

        #     for i in nums:
        #         if i == num:
        #             count += 1

        #     if count > len(nums) // 3:

        #         if num not in result:
        #             result.append(num)

        # return result

        #============ hash map sol ==================

        freq = {} #hash map(dictionary) where key : num in list, value : count of num

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
            
        result = []

        for n in freq:
            if freq[n] > len(nums)//3:
                result.append(n)
        
        return result