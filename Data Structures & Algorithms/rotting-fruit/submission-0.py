class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows , ncols = len(grid) , len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        time = 0 
        directions = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        # count the no of fresh oranges and include the rotten in queue 
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    fresh += 1 

                elif grid[r][c] == 2:
                    q.append((r , c))
                    visit.add((r , c))

        while q and fresh:
            for i in range(len(q)):
                row , col = q.popleft()
                for dr , dc in directions:
                    r , c = row + dr , col + dc
                    if 0 <= r < nrows and 0 <= c < ncols and grid[r][c] == 1 and (r , c) not in visit:
                        visit.add((r , c))
                        q.append((r , c))
                        grid[r][c] = 2
                        fresh -= 1 

            time += 1

        
        return time if not fresh else -1

        