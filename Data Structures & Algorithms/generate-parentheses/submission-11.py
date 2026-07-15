class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []

        def backtrack(n , openN , closeN):
            if n == openN == closeN:
                res.append("".join(stk))
                return 

            if n > openN:
                stk.append('(')
                backtrack(n , openN + 1 , closeN)
                stk.pop()
            
            if openN > closeN:
                stk.append(')')
                backtrack(n , openN , closeN + 1)
                stk.pop()

        backtrack(n , 0 , 0)
        return res