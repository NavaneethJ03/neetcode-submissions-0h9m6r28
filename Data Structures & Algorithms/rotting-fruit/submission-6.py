class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dirs = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    q.append([r , c])
        
        time = 0 

        while fresh and q:
            for _ in range(len(q)):
                row , col = q.popleft()
                for dr , dc in dirs:
                    nr , nc = dr + row , dc + col
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr , nc])
                        fresh -= 1 

            time += 1 
        
        return time if not fresh else -1