class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows , cols = len(board) , len(board[0])
        dirs = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]

        def dfs(r , c):
            stk = [[r , c]]
            board[r][c] = '.'
            while stk:
                r , c = stk.pop()
                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == 'O':
                        stk.append([nr , nc])
                        board[nr][nc] = '.'
            
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r , 0)
            if board[r][cols - 1] == 'O':
                dfs(r , cols - 1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0 , c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1 , c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = 'X'
                elif board[r][c] == '.':
                    board[r][c] = 'O'

        

