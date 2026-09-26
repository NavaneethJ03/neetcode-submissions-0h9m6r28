class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 

        count = Counter(hand)
        minHeap = [k for k , v in count.items()]
        heapq.heapify(minHeap)
        while minHeap:
            start = minHeap[0]
            for i in range(start , start + groupSize):
                if i not in count:
                    return False 
                count[i] -= 1 
                if count[i] == 0:
                    if minHeap[0] != i:
                        return False 
                    heapq.heappop(minHeap)
                    del count[i]
                
        return True