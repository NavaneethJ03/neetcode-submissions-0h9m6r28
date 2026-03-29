class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return None 
        nrows = len(grid)
        ncols = len(grid[0])
        maxArea = 0
        def dfs(r , c):
            directions = [(1 , 0) , (0 , 1) , (0 , -1), (-1 , 0)]

            stack = []
            stack.append((r , c))
            area = 0 
            while stack:
                row , col = stack.pop()          
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    area += 1 
                    for dr , dc in directions:
                        if (row + dr >= 0 and col + dc >= 0 and row + dr < nrows and col + dc < ncols):
                            stack.append((row + dr , col + dc))

            return area 

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea , dfs(r , c))

        return maxArea

        