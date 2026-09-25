# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point then reverse the second half and then merge 
        fast = slow = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next 
        slow.next = prev = None 
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp

        second = prev 
        first = head
        while first and second:
            temp1 , temp2 = first.next , second.next 
            first.next = second
            second.next = temp1 
            first = temp1 
            second = temp2 

        