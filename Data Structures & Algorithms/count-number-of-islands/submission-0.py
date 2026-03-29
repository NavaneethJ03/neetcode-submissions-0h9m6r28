class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0 
        def dfs(r , c):
            stk = []
            stk.append((r,c))
            direction = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
            while stk:
                row , col = stk.pop()
                if grid[row][col] == "1":
                    grid[row][col] = "0" 
                    for dr , dc in direction:
                        if dr + row in range(len(grid)) and dc + col in range(len(grid[0])):
                            stk.append((dr + row , dc + col))

            self.ans += 1 
            return None

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1": 
                    dfs(r , c)

        return self.ans