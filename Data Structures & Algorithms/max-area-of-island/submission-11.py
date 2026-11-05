class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        dirs = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        def dfs(r , c):
            stk = [[r , c]]
            area = 0 
            while stk:
                row , col = stk.pop()
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    area += 1 
                    for dr , dc in dirs:
                        nr , nc = dr + row , dc + col
                        if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] == 1:
                            stk.append([nr , nc])
                            visit.add((nr , nc))

            return area 

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans , dfs(r , c))


        return ans
                