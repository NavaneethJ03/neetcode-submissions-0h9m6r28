class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x , y in points:
            dist = x * x + y * y 
            heapq.heappush(minHeap , [-dist , [x , y]])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return list(minHeap[i][1] for i in range(k))