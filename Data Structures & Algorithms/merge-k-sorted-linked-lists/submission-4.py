# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merger(l1 , l2):
            dummy = ListNode(0)
            cur = dummy 

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    if l1:
                        l1 = l1.next
                else:
                    cur.next = l2
                    if l2:
                        l2 = l2.next
                cur = cur.next 

            cur.next = l1 or l2

            return dummy.next

        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            new = merger(l1 , l2)
            lists.append(new)

        return lists[0]

            