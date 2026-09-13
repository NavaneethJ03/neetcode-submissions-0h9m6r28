class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        dirs = [(1,0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r , c])
                    visit.add((r,c))
        dist = 0
        while q:
            for _ in range(len(q)):
                row , col = q.popleft()
                grid[row][col] = dist
                for dr , dc in dirs:
                    nr , nc = dr + row , dc + col
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] != -1 and (nr , nc) not in visit:
                        visit.add((nr , nc))
                        q.append([nr , nc])
            dist += 1 

        
