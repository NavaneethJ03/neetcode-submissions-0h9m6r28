class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap) * -1
            s2 = heapq.heappop(maxHeap) * -1
            diff = s1 - s2 
            if diff:
                heapq.heappush(maxHeap , diff * -1)

        return maxHeap[0] * -1 if maxHeap else 0
