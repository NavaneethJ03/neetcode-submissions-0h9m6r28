class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def dfs(o , c , n):
            if n == o == c:
                res.append("".join(stk))
                return 

            if o < n:
                stk.append('(')
                dfs(o + 1 , c , n)
                stk.pop()
            if c < o:
                stk.append(')')
                dfs(o , c + 1 , n)
                stk.pop()

        dfs(0 , 0 , n)
        return res