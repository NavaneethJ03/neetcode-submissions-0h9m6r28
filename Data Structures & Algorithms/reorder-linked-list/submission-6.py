# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0 , head)
        fast = slow = dummy 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next 
        slow.next = None 

        prev = None 
        curr = second
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp

        second = prev 
        first = dummy.next 

        while first and second:
            tmp1 , tmp2 = first.next , second.next 
            first.next = second
            second.next = tmp1 
            first = tmp1 
            second = tmp2

            