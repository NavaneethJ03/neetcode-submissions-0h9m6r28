class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1,0) , (0,-1) , (0,1) , (-1,0)]

        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0 
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist
                for dr , dc in dirs:
                    nr , nc = dr + r , dc + c
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] != -1:
                        q.append([nr ,nc])
                        visit.add((nr , nc))

            dist += 1 

        
                