class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for key , val in c.items():
            heap.append((-val , key))

        heapq.heapify(heap)
        ans = []
        for i in range(k):
            v , k = heapq.heappop(heap)
            ans.append(k)

        return ans

        
