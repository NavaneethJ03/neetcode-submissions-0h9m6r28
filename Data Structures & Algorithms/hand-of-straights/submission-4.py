class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first , first + groupSize):
                if i not in count:
                    return False 
                
                count[i] -= 1 

                if count[i] == 0:
                    if heap[0] != i: # means that we have another val which is lesser than the current val which is false 
                        return False 
                    
                    heapq.heappop(heap)

        return True