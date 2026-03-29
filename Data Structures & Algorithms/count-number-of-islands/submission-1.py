class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows , ncols = len(grid) , len(grid[0])
        self.ans = 0 
        directions = [(1,0) , (-1,0) ,(0 , 1) , (0 , -1)]
        def dfs(r , c):
            stack = []
            stack.append((r , c))

            while stack:
                row , col = stack.pop()
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    for dr , dc in directions:
                        r , c = row + dr , col + dc 
                        if 0 <= r < nrows and 0 <= c < ncols:
                            stack.append((r , c))

            self.ans += 1 


        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    dfs(r , c)

        return self.ans 