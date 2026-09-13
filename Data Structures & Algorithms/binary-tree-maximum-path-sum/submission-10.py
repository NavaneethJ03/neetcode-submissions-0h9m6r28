# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val

        def dfs(node):
            if not node:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)
            maxLeft = max(left , 0)
            maxRight = max(right , 0)
            self.ans = max(self.ans , maxLeft + maxRight + node.val)
            return max(maxLeft , maxRight) + node.val

        dfs(root)
        return self.ans
 