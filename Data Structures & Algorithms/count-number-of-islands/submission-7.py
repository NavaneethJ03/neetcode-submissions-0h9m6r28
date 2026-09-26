class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        
        def dfs(r , c):
            visit = set()
            stk = [[r , c]]
            grid[r][c] = '0'
            while stk:
                r , c = stk.pop()
                for dr , dc in dirs:
                    nr , nc = dr + r , c + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == '1':
                        stk.append([nr , nc])
                        grid[nr][nc] = '0'
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans += 1 
                    dfs(r , c)

        return ans


