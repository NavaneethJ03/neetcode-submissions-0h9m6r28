class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def dfs(n , openN , closeN):
            if openN == closeN == n:
                res.append("".join(stk))
                return 

            if openN < n:
                stk.append('(')
                dfs(n , openN + 1 , closeN)
                stk.pop()

            if closeN < openN:
                stk.append(')')
                dfs(n , openN , closeN + 1)
                stk.pop()

        dfs(n , 0 , 0)
        return res