class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        dirs = [(1 , 0) , (0 , 1) , (0 , -1) , (-1 , 0)]

        def dfs(r , c):
            stk = []
            stk.append([r , c])
            visit.add((r,c))
            while stk:
                r , c = stk.pop()
                grid[r][c] = "0"
                for dr , dc in dirs:
                    row , col = r + dr , c + dc
                    if (0 <= row < rows) and (0 <= col < cols) and grid[row][col] == '1' and (row , col) not in visit:
                        stk.append([row , col])
                        visit.add((row , col))

        ans = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans += 1 
                    dfs(r , c)
        return ans 
                

