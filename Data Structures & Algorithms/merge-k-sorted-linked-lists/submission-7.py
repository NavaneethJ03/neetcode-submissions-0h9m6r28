# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        cur = dummy 
        minHeap = []
        for i , l in enumerate(lists):
            if l:
                minHeap.append([l.val , i , l])
        heapq.heapify(minHeap)

        while minHeap:
            v , i , node = heapq.heappop(minHeap)
            cur.next = node 
            cur = cur.next 
            node = node.next
            if node:
                heapq.heappush(minHeap , [node.val , i , node])
            
        return dummy.next 


