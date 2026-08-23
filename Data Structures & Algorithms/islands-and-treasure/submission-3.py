class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi Source BFS 
        q = deque()
        rows , cols = len(grid) , len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r , c])
        dirs = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        visit = set()
        dist = 0 
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist
                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] == 2147483647:
                        q.append([nr , nc])
                        visit.add((nr , nc))
            dist += 1 
