class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        rows , cols = len(grid) , len(grid[0])
        minHeap = [[grid[0][0] , 0 , 0]]
        visit = set()
        while minHeap:
            time , r , c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            if r == rows - 1 and c == cols - 1:
                return time 

            visit.add((r,c))
            for dr , dc in dirs:
                nr , nc = dr + r , dc + c 
                if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit:
                    heapq.heappush(minHeap , [max(time , grid[nr][nc]) , nr , nc])