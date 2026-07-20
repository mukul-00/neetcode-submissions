# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         res = []
#         i = 0

#         for j in range(len(nums)):

#             if j - i + 1 == k:

#                 res.append(max(nums[i:j + 1]))
#                 i += 1

#         return res


#============================================================================
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        res = []

        i = 0

        for j in range(len(nums)):

            # Remove all smaller elements from the back
            while dq and dq[-1] < nums[j]:
                dq.pop()

            # Add current value
            dq.append(nums[j])

            # Window is complete
            if j - i + 1 == k:

                # Front is the maximum
                res.append(dq[0])

                # Remove the outgoing value if it is at the front
                if dq[0] == nums[i]:
                    dq.popleft()

                i += 1

        return res


#============================================================================
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

#         i = 0
#         res = []
#         dq = deque()

#         for j in range(len(nums)):

#             while dq and nums[dq[-1]] < nums[j]:
#                 dq.pop()
            
#             dq.append(j)

#             if dq[0] < i:
#                 dq.popleft()
            
#             if j - i + 1 == k:
#                 res.append(nums[dq[0]])

#                 i += 1
        
#         return res