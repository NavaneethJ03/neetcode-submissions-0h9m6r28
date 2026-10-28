# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(root):
            if not root:
                return "$"

            return '^' + str(root.val) + preorder(root.left) + preorder(root.right)

        s1 = preorder(p)
        s2 = preorder(q)

        return s1 == s2