class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0 
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        def dfs(r , c):
            stk = [[r , c]]
            grid[r][c] = 0
            curArea = 0
            while stk:
                row , col = stk.pop()
                curArea += 1 
                self.area = max(self.area , curArea)
                for dr , dc in dirs:
                    nr , nc = row + dr , col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        stk.append([nr , nc])
                        grid[nr][nc] = 0
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r , c)

        return self.area

