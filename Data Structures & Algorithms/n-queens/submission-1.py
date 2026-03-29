class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        pos = set()
        neg = set()
        col = set()

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if (r + c) in pos or (r - c) in neg or board[r][c] == "Q" or c in col:
                    continue 

                board[r][c] = "Q"
                pos.add(r + c)
                neg.add(r - c)
                col.add(c)
                dfs(r + 1)
                board[r][c] = "."
                pos.remove(r + c)
                neg.remove(r - c)
                col.remove(c)

        dfs(0)

        return res 


            