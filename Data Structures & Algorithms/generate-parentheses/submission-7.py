class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def backtrack(openN , closeN , n):
            if openN == closeN == n:
                res.append("".join(stk))
                return 

            if openN < n:
                stk.append("(")
                backtrack(openN + 1 , closeN , n)
                stk.pop()

            if closeN < openN:
                stk.append(")")
                backtrack(openN , closeN + 1 , n)
                stk.pop()

            
        backtrack(0 , 0 , n)
        return res 
