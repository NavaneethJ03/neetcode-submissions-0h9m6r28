class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        fresh = 0 
        time = 0 
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==  1:
                    fresh += 1 

                elif grid[r][c] == 2:
                    q.append((r,c))


        while fresh and q:
            time += 1 
            for _ in range(len(q)):
                row , col = q.popleft()
                for dr , dc in dirs:
                    nr , nc = dr + row , dc + col 
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        fresh -= 1 
                        q.append((nr , nc))
                        grid[nr][nc] = 2 



        return time if fresh == 0 else -1
