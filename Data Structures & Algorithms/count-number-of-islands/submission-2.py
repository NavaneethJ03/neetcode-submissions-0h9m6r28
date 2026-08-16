class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows , ncols = len(grid) , len(grid[0])
        self.count = 0 
        dirs = [(0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0)]
        def dfs(r , c):
            stk = []
            stk.append([r , c])
            while stk:
                row , col = stk.pop()
                grid[row][col] = '0'
                for dr , dc in dirs:
                    nr , nc = row + dr , col + dc
                    if (0 <= nr < nrows) and (0 <= nc < ncols) and grid[nr][nc] == '1':
                        stk.append([nr , nc])

            self.count += 1

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == '1':
                    dfs(r , c)

        return self.count


