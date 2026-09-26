class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap , num)
        else:
            heapq.heappush(self.maxHeap , -num)
            
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap , -val)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap , -val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]