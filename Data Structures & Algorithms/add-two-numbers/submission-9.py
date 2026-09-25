# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        while carry or l1 or l2:
            v1 = l1.val if l1 else 0 
            if l1:
                l1 = l1.next
            v2 = l2.val if l2 else 0 
            if l2:
                l2 = l2.next
            val = carry + v1 + v2 
            carry = val // 10
            val = val % 10
            node = ListNode(val)
            cur.next = node
            cur = cur.next 

        return dummy.next 