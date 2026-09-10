# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point then reverse the second half and then merge 
        dummy = ListNode(0 , head)
        slow = fast = dummy
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        second = slow.next 
        slow.next = None 
        prev = None 
        while second:
            temp = second.next 
            second.next = prev 
            prev = second
            second = temp
        second = prev
        first = dummy.next
        while second:
            temp1 , temp2 = first.next , second.next 
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2 
            



        

            