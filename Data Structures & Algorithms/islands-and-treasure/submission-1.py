class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        nrows , ncols = len(grid) , len(grid[0])
        visit = set()
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    q.append((r , c))
                    visit.add((r,c))

        def addcell(r , c):
            if 0 <= r < nrows and 0 <= c < ncols and grid[r][c] != -1 and (r,c) not in visit:
                q.append((r , c))
                visit.add((r , c))

        dist = 0 
        while q:
            for _ in range(len(q)):
                row , col = q.popleft()
                grid[row][col] = dist
                addcell(row + 1 , col)
                addcell(row - 1 , col)
                addcell(row , col + 1)
                addcell(row , col - 1)

            dist += 1 




