# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # count = 0
        # self.res = None
        # def inorder(node):
        #     nonlocal count
        #     if not node:
        #         return 
            
        #     inorder(node.left)
        #     count += 1 
        #     if count == k:
        #         self.res = node.val

        #     inorder(node.right)

        # inorder(root)
        # return self.res
        inorder = []
        cur = root
        stk = []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            node = stk.pop()
            inorder.append(node.val)
            if node.right:
                cur = node.right

        return inorder[k-1]