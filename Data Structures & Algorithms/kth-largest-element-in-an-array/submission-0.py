class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            if len(minHeap) >= k:
                heapq.heappushpop(minHeap , num)
            else:
                heapq.heappush(minHeap , num)

        return minHeap[0]
