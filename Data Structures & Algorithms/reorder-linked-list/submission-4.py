# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        mid = slow.next 
        slow.next = None # break the connection 

        prev = None 
        curr = mid 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp

        mid = prev 
        first = head

        while mid:
            temp1 , temp2 = first.next , mid.next
            first.next = mid 
            mid.next = temp1 
            first = temp1 
            mid = temp2



        
