# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        grp_prev = dummy
        while True:
            kthNode = self.findKth(grp_prev , k)
            if not kthNode:
                return dummy.next
            kthNext = prev = kthNode.next 
            cur = grp_prev.next
            while cur != kthNext:
                temp = cur.next 
                cur.next = prev 
                prev = cur
                cur = temp 
            
            temp = grp_prev.next 
            grp_prev.next = kthNode
            grp_prev = temp
        
    def findKth(self , head , k):
        cur = head 
        for _ in range(k):
            if cur:
                cur = cur.next 
            else:
                return None 
        
        return cur

