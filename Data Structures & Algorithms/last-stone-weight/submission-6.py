class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-v for v in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            diff = s1 - s2
            if diff:
                heapq.heappush(maxHeap , diff)
            
        if maxHeap:
            return -maxHeap[0]
        return 0