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
            kth = self.findKthNode(groupPrv , k)
            if not kth:
                break
            kthNext = kth.next 
            curr = groupPrv.next 
            prv = kthNext
            while curr != kthNext:
                temp = curr.next
                curr.next = prv 
                prv = curr 
                curr = temp
            temp = groupPrv.next
            groupPrv.next = kth
            groupPrv = temp

        return dummy.next

    def findKthNode(self, node , k):
        curr = node
        for _ in range(k):
            if not curr:
                return None
            curr = curr.next

        return curr