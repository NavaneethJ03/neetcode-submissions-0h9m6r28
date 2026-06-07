class MedianFinder:

    def __init__(self):
        self.minHeap , self.maxHeap = [] , []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > self.maxHeap[0] * -1:
            heapq.heappush(self.minHeap , num)
        else:
            heapq.heappush(self.maxHeap , -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap , -val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap , -val)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((self.maxHeap[0] * -1) + self.minHeap[0]) / 2

        return self.maxHeap[0] * -1 if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        
        