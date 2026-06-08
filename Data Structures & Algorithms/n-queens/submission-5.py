class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set()
        negDiag = set()
        cols = set()

        board = [["."] * n  for i in range(n)]

        def backtrack(r):
            if r >= n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if r + c in posDiag or r - c in negDiag or c in cols:
                    continue 

                posDiag.add(r + c)
                negDiag.add(r - c)
                cols.add(c)
                board[r][c] = "Q"
                backtrack(r + 1)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)
                board[r][c] = "."

        backtrack(0)
        return res 
