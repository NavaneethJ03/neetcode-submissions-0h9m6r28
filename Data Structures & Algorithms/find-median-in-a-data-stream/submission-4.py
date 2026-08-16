class MedianFinder:

    def __init__(self):
        self.maxHeap , self.minHeap = [] , []

    def addNum(self, num: int) -> None:
        if self.maxHeap and self.maxHeap[0] * -1 < num:
            heapq.heappush(self.minHeap , num)
        else:
            heapq.heappush(self.maxHeap , num * -1)

        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                n = heapq.heappop(self.maxHeap) * -1
                heapq.heappush(self.minHeap , n)
            else:
                n = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap , n * -1)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]

        else:
            return float(((self.maxHeap[0] * -1) + self.minHeap[0]) / 2)
        
        