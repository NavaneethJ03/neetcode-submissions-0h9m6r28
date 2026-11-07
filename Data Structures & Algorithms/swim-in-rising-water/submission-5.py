class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid)
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        minHeap = [[grid[0][0] , 0 , 0]]
        visit = set()
        while minHeap:
            w , r , c = heapq.heappop(minHeap)
            if (r , c) not in visit:
                if r == c == rows - 1:
                    return w
                visit.add((r,c))
                for dr , dc in dirs:
                    nr , nc = dr + r , dc + c
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit:
                        heapq.heappush(minHeap , [max(w , grid[nr][nc]) , nr , nc])

