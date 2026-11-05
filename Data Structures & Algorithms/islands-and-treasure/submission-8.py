class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        dirs = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r , c])
        dist = 0
        while q:
            for _ in range(len(q)):
                row , col = q.popleft()
                if (row , col) not in visit:
                    visit.add((row , col))
                    grid[row][col] = dist 
                    for dr , dc in dirs:
                        nr , nc = dr + row , dc + col 
                        if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] != -1:
                            q.append([nr , nc])

            dist += 1 

        