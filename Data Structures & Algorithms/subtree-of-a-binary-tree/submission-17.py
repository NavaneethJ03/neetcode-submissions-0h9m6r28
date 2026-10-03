# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node:
                return "N"
            
            return str(node.val) + preorder(node.left) + preorder(node.right)

        s1 = preorder(root)
        s2 = preorder(subRoot)

        if s2 in s1:
            return True
        
        return False
