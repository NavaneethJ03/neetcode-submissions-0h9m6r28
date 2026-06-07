class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            s1 = heapq.heappop(maxHeap) * -1
            s2 = heapq.heappop(maxHeap) * -1
            diff = abs(s1 - s2)
            if diff:
                heapq.heappush(maxHeap , -diff)
            
        return -1 * maxHeap[0] if maxHeap else 0