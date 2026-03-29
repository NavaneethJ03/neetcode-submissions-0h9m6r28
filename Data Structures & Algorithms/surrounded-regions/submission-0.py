class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrows , ncols = len(board) , len(board[0])
        directions = [(1 , 0) , (-1,0) , (0,1) , (0,-1)]
        def dfs(r , c):
            stack = []
            stack.append((r , c))
            board[r][c] = "#"
            while stack:
                row , col = stack.pop()
                for dr , dc in directions:
                    r , c = row + dr , col + dc 
                    if 0 <= r < nrows and 0 <= c < ncols and board[r][c] == "O":
                        board[r][c] = "#"
                        stack.append((r , c))

        for r in range(nrows):
            if board[r][0] == "O":
                dfs(r , 0)
            if board[r][ncols -1] == "O":
                dfs(r , ncols - 1)

        for c in range(ncols):
            if board[0][c] == "O":
                dfs(0 , c)
            if board[nrows - 1][c] == "O":
                dfs(nrows - 1 , c)

        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"