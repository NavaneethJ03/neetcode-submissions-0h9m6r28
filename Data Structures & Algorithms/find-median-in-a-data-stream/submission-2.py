class MedianFinder:

    def __init__(self):
        self.MaxHeap , self.MinHeap = [] , []

    def addNum(self, num: int) -> None:
        if self.MinHeap and num > self.MinHeap[0]:
            heapq.heappush(self.MinHeap , num)
        else:
            heapq.heappush(self.MaxHeap , -1 * num)

        if len(self.MinHeap) > len(self.MaxHeap) + 1:
            val = heapq.heappop(self.MinHeap)
            heapq.heappush(self.MaxHeap , -1 * val)

        if len(self.MaxHeap) > len(self.MinHeap) + 1:
            val = heapq.heappop(self.MaxHeap)
            heapq.heappush(self.MinHeap , -1 * val)

    def findMedian(self) -> float:
        if len(self.MaxHeap) > len(self.MinHeap):
            return self.MaxHeap[0] * -1

        if len(self.MinHeap) > len(self.MaxHeap):
            return self.MinHeap[0]

        else:
            return (self.MinHeap[0] + self.MaxHeap[0] * -1 ) / 2
        