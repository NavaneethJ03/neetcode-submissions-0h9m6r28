class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        land = 2147483647
        visit = set()
        q = deque()
        dist = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append((r , c))
        def addRoom(r , c):
            if 0 <= r < rows and 0 <= c < cols and (r , c) not in visit and grid[r][c] != -1:
                visit.add((r , c))
                q.append((r , c))

        while q:
            for i in range(len(q)):
                row , col = q.popleft()
                grid[row][col] = dist
                addRoom(row , col + 1)
                addRoom(row + 1 , col)
                addRoom(row - 1 , col)
                addRoom(row , col - 1)
            dist += 1 




            



