class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h , 0)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start , start + groupSize):
                if i not in count:
                    return False 
                else:
                    count[i] -= 1 
                    if count[i] == 0:
                        if minHeap[0] != i:
                            return False 
                        heapq.heappop(minHeap)

        return True