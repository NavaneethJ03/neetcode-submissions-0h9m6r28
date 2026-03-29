class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1 
        cols = len(matrix[0]) - 1 

        top , bottom = 0 , rows
        l , r = 0 , cols

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break 

        while l <= r :
            m = (r + l) // 2 
            if target == matrix[row][m]:
                return True 
            elif target > matrix[row][m]:
                l = m + 1 
            else :
                r = m - 1 

        return False 
