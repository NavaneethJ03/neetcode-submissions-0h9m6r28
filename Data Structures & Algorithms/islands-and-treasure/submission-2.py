class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r , c))
                    visit.add((r , c))

        cur_dist = 0 

        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                if grid[r][c] > cur_dist:
                    grid[r][c] = cur_dist

                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] != -1 and (nr , nc) not in visit:
                        q.append((nr , nc))
                        visit.add((nr , nc))
            cur_dist += 1 


    