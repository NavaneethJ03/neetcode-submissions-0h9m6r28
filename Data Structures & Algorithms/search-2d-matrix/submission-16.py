class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom , right = len(matrix) - 1, len(matrix[0]) - 1
        top = left = 0

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not(top <= bottom):
            return False 

        while left <= right:
            m = (left + right) // 2 
            if target < matrix[row][m]:
                right = m - 1 
            elif target > matrix[row][m]:
                left = m + 1 
            else:
                return True

        return False 

