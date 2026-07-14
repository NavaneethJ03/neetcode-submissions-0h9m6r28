class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bottom = 0 , len(matrix) - 1
        left , right = 0 , len(matrix[0]) - 1 

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bottom = row - 1 
            else:
                break

        if not (top <= bottom):
            return False 

        while left <= right:
            m = (left + right) // 2 
            if matrix[row][m] == target:
                return True 
            elif matrix[row][m] > target:
                right = m - 1 
            else:
                left = m + 1 

        return False 