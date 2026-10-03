class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap , num)
        else:
            heapq.heappush(self.maxHeap , -num)
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap , -val)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap , -val)

    def findMedian(self) -> float:
        
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]