class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def dfs(openN , closeN , n):
            if openN == closeN == n:
                copy = "".join(stk)
                res.append(copy)
                return 

            if openN < n:
                stk.append("(")
                dfs(openN + 1 , closeN , n)
                stk.pop()

            if closeN < openN:
                stk.append(")")
                dfs(openN , closeN + 1 , n)
                stk.pop()

        dfs(0 , 0 , n)
        return res 