class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0 
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        visit = set()
        def dfs(r , c):
            stk = [[r , c]]
            while stk:
                row , col = stk.pop()
                grid[row][col] = '0'
                for dr , dc in dirs:
                    nr , nc = dr + row , dc + col
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == '1':
                        stk.append([nr , nc])

        
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r , c)
                    ans += 1 

        return ans