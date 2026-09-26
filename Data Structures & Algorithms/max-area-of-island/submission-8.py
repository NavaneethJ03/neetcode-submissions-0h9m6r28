class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0 
        rows , cols = len(grid) , len(grid[0])
        dirs = [[1,0] , [0,1] , [-1,0] , [0,-1]]

        def bfs(r , c):
            q = deque([[r , c]])
            area = 0 
            grid[r][c] = 0
            while q:
                for _ in range(len(q)):
                    row , col = q.popleft()
                    area += 1
                    for dr , dc in dirs:
                        nr , nc = row + dr , col + dc 
                        if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                            grid[nr][nc] = 0 
                            q.append([nr , nc])

            self.ans = max(self.ans , area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r , c)

        return self.ans 