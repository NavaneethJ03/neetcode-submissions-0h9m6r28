# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        count = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += 1 

        return count
                
        # res = 0

        # stk = [[root , 1]]

        # while stk:
        #     node , height = stk.pop()
        #     res = max(res , height)
        #     if node.left:
        #         stk.append([node.left , height + 1])
        #     if node.right:
        #         stk.append([node.right , height + 1])

            

        # return res 



        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left , right) + 1 
        