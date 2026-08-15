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

        def merge(lists , left , right):
            if left == right:
                return lists[left]

            m = (left + right) // 2
            l1 = merge(lists , left , m)
            l2 = merge(lists , m + 1 , right)

            return merger(l1 , l2)

        return merge(lists , 0 , len(lists) - 1)
            