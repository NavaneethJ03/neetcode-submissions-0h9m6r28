# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        grpPrev = dummy 
        while True:
            KthNode = self.findKth(grpPrev , k)
            if not KthNode:
                break
            grpNext = prev = KthNode.next 
            curr = grpPrev.next 
            while curr != grpNext:
                temp = curr.next 
                curr.next = prev
                prev = curr 
                curr = temp 
            temp1 = grpPrev.next
            grpPrev.next = prev 
            grpPrev = temp1

        return dummy.next

    def findKth(self , node , k):
        curr = node
        for _ in range(k):
            if not curr:
                return None
            curr = curr.next
        return curr
        