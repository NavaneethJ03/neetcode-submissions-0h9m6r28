# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        # Find the middle of the LL
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        # Alter the connections 
        second = slow.next 
        slow.next = prev = None 

        # reverse the second LL 
        while second:
            temp = second.next 
            second.next = prev 
            prev = second
            second = temp 

        second = prev 
        first = head 

        # merge LL 's 
        while second:
            temp1 , temp2 = first.next , second.next 
            first.next = second 
            second.next = temp1 
            first , second = temp1 , temp2 

        