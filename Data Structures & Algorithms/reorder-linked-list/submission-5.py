# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head 
        fast = head.next 
        # finding the mid
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        second = slow.next 
        slow.next = None 
        curr = second
        prev = None 
    # reverse the second half 
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp

        second = prev 
        first = head 
        # merge the two halves 
        while first and second:
            tmp1 , tmp2 = first.next , second.next
            first.next = second 
            second.next = tmp1
            first = tmp1 
            second = tmp2 

        





            






