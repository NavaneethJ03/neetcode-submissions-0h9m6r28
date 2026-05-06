# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val 

        def dfs(node):
            if not node:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left , 0)
            right = max(right , 0)

            self.res = max(self.res , left + right + node.val)

            return max(left , right) + node.val

        dfs(root)
        return self.res 