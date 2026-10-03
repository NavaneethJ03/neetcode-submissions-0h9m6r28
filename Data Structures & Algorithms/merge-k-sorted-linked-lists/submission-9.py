# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        dummy = ListNode(0)
        cur = dummy 

        minHeap = [[l.val , i , l] for i , l in enumerate(lists) if l is not None]
        heapq.heapify(minHeap)

        while minHeap:
            v , idx , L = heapq.heappop(minHeap)
            cur.next = L
            if L.next:
                heapq.heappush(minHeap , [L.next.val , idx , L.next])
            cur = cur.next 

        return dummy.next
        


        