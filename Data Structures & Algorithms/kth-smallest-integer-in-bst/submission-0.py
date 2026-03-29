# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(root):
            res = []
            q = deque([root])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return res 

        arr = bfs(root)
        arr.sort()
        return arr[k-1]


