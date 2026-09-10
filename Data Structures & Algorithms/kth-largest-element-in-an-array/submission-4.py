class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        c = 1
        while c < k:
            heapq.heappop(heap)
            c += 1 
        return heap[0] *-1

