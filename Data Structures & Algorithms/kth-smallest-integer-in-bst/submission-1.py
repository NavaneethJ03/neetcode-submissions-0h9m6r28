# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return None
            nonlocal res
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

            return res 

        arr = inorder(root)
        print(arr)
        return arr[k-1]
            


