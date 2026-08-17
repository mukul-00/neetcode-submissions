class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def solve(open, close, s):

            # base case
            if open == close and open+close == n*2:
                res.append(s)
                return 
            
            # conditions then call recursion
            if open < n:
                solve(open+1, close, s + "(")
            if close < open:
                solve(open, close+1, s + ")")
            
        solve(0, 0, "")

        return res