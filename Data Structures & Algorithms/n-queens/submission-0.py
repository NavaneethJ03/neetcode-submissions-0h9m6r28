class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positiveDiag = set()
        negativeDiag = set()
        res = []
        board = [['.'] * n for _ in range(n)]
        print(board)
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in positiveDiag or (r-c) in negativeDiag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                positiveDiag.add(r+c)
                negativeDiag.add(r-c)
                backtrack(r + 1)
                cols.remove(c)
                positiveDiag.remove(r+c)
                negativeDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res
