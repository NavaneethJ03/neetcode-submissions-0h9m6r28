class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0 
        rows , cols = len(grid) , len(grid[0])
        dirs = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        visit = set()
        def dfs(r , c):
            area = 0 
            stk = [[r , c]]
            visit.add((r , c))
            while stk:
                r , c = stk.pop()
                grid[r][c] = 0
                area += 1 
                self.ans = max(self.ans , area)
                for dr , dc in dirs:
                    nr , nc = dr + r , dc + c
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] == 1:
                        stk.append([nr , nc])
                        visit.add((nr , nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r , c)

        return self.ans

                

