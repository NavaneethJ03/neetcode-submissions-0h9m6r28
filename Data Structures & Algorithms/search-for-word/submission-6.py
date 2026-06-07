class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        def dfs(i , r , c):
            if i >= len(word):
                return True 

            if not(0 <= r < rows) or not(0 <= c < cols) or (r , c) in visit or board[r][c] != word[i]:
                return False 
            visit.add((r,c))
            res = dfs(i + 1 , r + 1 , c) or dfs(i + 1 , r - 1 , c) or dfs(i + 1 , r , c + 1) or dfs(i + 1 , r , c - 1)
            visit.remove((r,c))
            return res 


        for r in range(rows):
            for c in range(cols):
                if dfs(0 , r , c):
                    return True 


        return False 
