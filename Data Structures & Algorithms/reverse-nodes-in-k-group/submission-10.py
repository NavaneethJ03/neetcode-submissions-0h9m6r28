# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        groupPrv = dummy

        while True:
            kthNode = self.findKthNode(groupPrv , k)
            if not kthNode:
                break
            groupNxt = prev = kthNode.next 
            cur = groupPrv.next

            while cur != groupNxt:
                temp = cur.next
                cur.next = prev 
                prev = cur
                cur = temp
            temp = groupPrv.next
            groupPrv.next = prev 
            groupPrv = temp

        return dummy.next

    def findKthNode(self, node , k):
        cur = node
        for i in range(k):
            if cur:
                cur = cur.next 

        return cur