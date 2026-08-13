class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        visit = set()
        
        def backtrack(i , r , c):
            if i == len(word):
                return True 

            if not(0 <= r < rows) or not(0 <= c < cols) or (r , c) in visit or word[i] != board[r][c]:
                return False 

            visit.add((r , c))
            res = backtrack(i + 1 , r + 1, c) or backtrack(i + 1 , r - 1 , c) or backtrack(i + 1 , r , c - 1) or backtrack(i + 1 , r , c + 1)
            visit.remove((r , c))

            return res 

        for r in range(rows):
            for c in range(cols):
                if backtrack(0 , r , c):
                    return True

        return False 