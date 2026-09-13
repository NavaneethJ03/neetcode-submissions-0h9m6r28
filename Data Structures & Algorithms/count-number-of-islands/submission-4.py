class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0 
        dirs = [(1,0) , (0 , 1) , (-1,0) , (0 , -1)]
        rows , cols = len(grid) , len(grid[0])
        # visit = set()
        
        def dfs(r , c):
            stk = []
            stk.append([r , c])
            # visit.add((r,c))
            grid[r][c] = '0'
            while stk:
                row , col = stk.pop()
                for dr , dc in dirs:
                    nr , nc = row + dr , col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == '1':
                        stk.append([nr , nc])
                        grid[nr][nc] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r , c)
                    self.count += 1 
        return self.count