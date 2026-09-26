class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows , cols = len(matrix) , len(matrix[0])
        visit = set()
        def dfs(r , c , prevVal):
            if not (0 <= r < rows) or not (0 <= c < cols) or matrix[r][c] <= prevVal:
                return 0 
            if (r , c) in memo:
                return memo[(r , c)]
            
            res = 1 
            res = max(res , 
                dfs(r + 1 , c , matrix[r][c]) + 1, 
                dfs(r , c + 1 , matrix[r][c]) + 1, 
                dfs(r - 1 , c , matrix[r][c]) + 1, 
                dfs(r , c - 1 , matrix[r][c]) + 1)

            memo[(r , c)] = res 
            return memo[(r , c)]

        for r in range(rows):
            for c in range(cols):
                dfs(r , c , -1)

        return max(memo.values())


            