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

            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            maxLeft = max(maxLeft , 0)
            maxRight = max(maxRight , 0)

            self.res = max(self.res , node.val + maxLeft + maxRight)

            return max(maxLeft , maxRight) + node.val

        dfs(root)
        return self.res 