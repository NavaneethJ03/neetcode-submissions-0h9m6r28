class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def backtrack(openN , closeN):
            if openN == closeN == n:
                res.append("".join(stk))
                return 

            if openN < n:
                stk.append("(")
                backtrack(openN + 1 , closeN)
                stk.pop()

            if closeN < openN:
                stk.append(")")
                backtrack(openN , closeN + 1)
                stk.pop()

        backtrack(0 , 0)

        return res 


