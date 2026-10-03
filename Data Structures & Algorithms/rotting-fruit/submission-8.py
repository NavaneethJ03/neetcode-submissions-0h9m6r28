class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        time = 0 
        while fresh and q:
            for i in range(len(q)):
                r , c = q.popleft()
                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        q.append([nr , nc])
                        grid[nr][nc] = 2
                        fresh -= 1 
            time += 1 
        return time if not fresh else -1
