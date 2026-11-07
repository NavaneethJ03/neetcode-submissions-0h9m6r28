class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows , cols = len(matrix) , len(matrix[0])
        top , bot = 0 , rows
        left , right = 0 , cols

        while top < bot and left < right:
            for i in range(left , right):
                res.append(matrix[top][i])
            top += 1 
            for i in range(top , bot):
                res.append(matrix[i][right - 1])
            right -= 1 
            
            if not(top < bot) or not (left < right):
                break

            for i in range(right - 1 , left - 1 , -1):
                res.append(matrix[bot - 1][i])
            bot -= 1 
            for i in range(bot - 1 , top - 1 , -1):
                res.append(matrix[i][left])
            left += 1

        return res