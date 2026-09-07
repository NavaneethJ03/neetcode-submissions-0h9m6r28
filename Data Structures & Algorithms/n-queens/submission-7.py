class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        negDiag = set()
        posDiag = set()
        cols = set()
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if r + c in posDiag or r - c in negDiag or c in cols:
                    continue

                negDiag.add(r - c)
                posDiag.add(r + c)
                cols.add(c)
                board[r][c] = 'Q'
                dfs(r + 1)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                cols.remove(c)
                board[r][c] = "."
        
        dfs(0)
        return res

        
