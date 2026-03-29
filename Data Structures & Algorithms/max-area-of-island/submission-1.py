class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0 
        nrows , ncols = len(grid) , len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r , c):
            stack = []
            stack.append((r , c))
            area = 0
            while stack:
                row , col = stack.pop()
                if grid[row][col] == 1:
                    area += 1 
                    grid[row][col] = 0 

                    for dr , dc in directions:
                        r , c = row + dr , col + dc
                        if 0 <= r < nrows and 0 <= c < ncols:
                            stack.append((r , c))

            self.res = max(self.res , area)

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    dfs(r , c)

        return self.res 