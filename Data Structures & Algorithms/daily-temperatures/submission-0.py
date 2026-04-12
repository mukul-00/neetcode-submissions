class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Next greatest to right(NGR)

        n = len(temperatures)

        st = []
        ans = n * [0]

        n = len(temperatures)

        for i in range(n - 1, -1, -1):

            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()

            if len(st) == 0:
                ans[i] = 0
            
            else:
                ans[i] = st[-1] - i

            st.append(i)
        
        return ans

