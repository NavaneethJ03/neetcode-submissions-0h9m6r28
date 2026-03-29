"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head 
        hmap = {None : None}

        while cur: # we create copy nodes and store them in the hashmap 
            copy = Node(cur.val)
            hmap[cur] = copy 
            cur = cur.next 

        cur = head 

        while cur: # here we assign the next pointers and the random pointers to the copies
            copy = hmap[cur]
            copy.next = hmap[cur.next]
            copy.random = hmap[cur.random]

            cur = cur.next 

        return hmap[head]