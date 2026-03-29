# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeL(l1 , l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next 
                else:
                    curr.next = l2 
                    l2 = l2.next 
                    
                curr = curr.next 

            curr.next = l1 or l2 

            return dummy.next 

        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            a = mergeL(l1 , l2)
            lists.append(a)

        return lists[0]
