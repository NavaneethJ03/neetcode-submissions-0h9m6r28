class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bot = 0 , len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2 
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        else:
            return False 

        l , r = 0 , len(matrix[0]) - 1 
        while l <= r:
            m = (l + r) // 2 
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m + 1 
            else:
                r = m - 1
        return False 