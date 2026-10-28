# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        minHeap = [[l.val , i , l] for i , l in enumerate(lists) if l is not None]
        heapq.heapify(minHeap)
        dummy = ListNode(0)
        cur = dummy
        while minHeap:
            val , idx , L = heapq.heappop(minHeap)
            cur.next = L
            cur = cur.next
            if L.next:
                heapq.heappush(minHeap , [L.next.val , idx , L.next])

        return dummy.next
