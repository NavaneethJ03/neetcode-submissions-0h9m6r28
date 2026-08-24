class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid)
        visit = set()
        dirs = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        minHeap = [[grid[0][0] , 0 , 0]]
        visit.add((0 , 0))
        while minHeap:
            w , r , c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return w
            for dr , dc in dirs:
                nr , nc = r + dr , c + dc 
                if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit:
                    heapq.heappush(minHeap , [max(w , grid[nr][nc]) ,nr ,nc])
                    visit.add((nr , nc))

        

        




        