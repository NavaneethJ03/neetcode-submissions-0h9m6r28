class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        dirs = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r , c])
                    visit.add((r,c))
        dist = 1
        while q:
            for _ in range(len(q)):
                row , col = q.popleft()
                for dr , dc in dirs:
                    nr , nc = row + dr , col + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr ,nc) not in visit and grid[nr][nc] != -1:
                        grid[nr][nc] = dist
                        q.append([nr , nc])
                        visit.add((nr ,nc))
            dist += 1 
