class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set()
        negDiag = set()
        cols = set()
        board = [["."]*n for _ in range(n)]

        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue 
                
                board[r][c] = 'Q'
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)
                dfs(r + 1)
                board[r][c] = "."
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)

        dfs(0)
        return res 
