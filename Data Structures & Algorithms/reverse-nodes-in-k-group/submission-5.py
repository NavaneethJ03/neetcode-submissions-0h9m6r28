# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        groupPrev = dummy 

        while True:
            kth = self.getK(groupPrev , k)
            if not kth:
                break 

            groupNext = kth.next 
            curr = groupPrev.next 
            prev = kth.next 

            while curr != groupNext:
                temp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = temp 

            temp = groupPrev.next # storing the prev start of the list and current end of the list
            groupPrev.next = kth # making the connection between the dummy and the new link formed 
            groupPrev = temp # shifting the groupPrev for the next group 


        return dummy.next 


            






















    def getK(self , node , k): 
        curr = node
        for _ in range(k):
            if curr:
                curr = curr.next 
            
        return curr 


