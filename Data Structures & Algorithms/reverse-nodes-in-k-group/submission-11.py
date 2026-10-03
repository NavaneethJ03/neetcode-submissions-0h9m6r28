# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0 , head)
        groupPrev = dummy 
        while True:
            kthNode = self.findKth(groupPrev , k)
            if not kthNode:
                break
            kthNext = kthNode.next 
            prev = kthNext
            cur = groupPrev.next 
            while cur != kthNext:
                temp = cur.next
                cur.next = prev 
                prev = cur 
                cur = temp 

            temp = groupPrev.next 
            groupPrev.next = prev 
            groupPrev = temp
        return dummy.next
    def findKth(self , start , k):
        cur = start
        for _ in range(k):
            if cur:
                cur = cur.next 
            else:
                break
        return cur 