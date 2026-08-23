class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        time = 0
        fresh = 0 
        q = deque()
        visit = set()
        dirs = [(1,0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r , c])
                    visit.add((r , c))
                elif grid[r][c] == 1:
                    fresh += 1 
        
        while fresh and q:
            for _ in range(len(q)):
                r , c = q.popleft()
                # grid[r][c] = 2
                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and grid[nr][nc] == 1:
                        q.append([nr , nc])
                        visit.add((nr , nc))
                        fresh -= 1 

            time += 1 

        return time if not fresh else -1
                

