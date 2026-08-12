# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = []
        stk.append([root , 1])
        ans = 1
        while stk:
            node , h = stk.pop()
            ans = max(ans , h)
            if node.left:
                stk.append([node.left , h + 1])
            if node.right:
                stk.append([node.right , h + 1])

        return ans

        