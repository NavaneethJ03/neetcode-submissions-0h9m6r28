# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self , node , k):
        curr = node
        for i in range(k - 1):
            if curr:
                curr = curr.next 

        return curr if curr else None 
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        groupPrev = dummy 

        while True:
            Kth = self.getKth(groupPrev.next , k)
            if not Kth:
                break

            KthNext = Kth.next 
            prev = Kth.next 

            curr = groupPrev.next

            while curr != KthNext:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp

            temp = groupPrev.next 
            groupPrev.next = Kth
            groupPrev = temp 

        return dummy.next
        