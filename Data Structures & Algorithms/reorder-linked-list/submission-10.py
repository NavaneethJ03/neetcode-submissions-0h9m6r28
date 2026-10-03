# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next 
        slow.next = None 
        prev = None 
        cur = second
        while cur:
            temp = cur.next 
            cur.next = prev 
            prev = cur
            cur = temp

        second = prev 
        first = head 

        while first and second:
            tmp1 , tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1 
            first = tmp1 
            second = tmp2 
        