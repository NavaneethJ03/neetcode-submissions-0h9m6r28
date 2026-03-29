class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix) - 1 

        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1 
            elif target > matrix[row][-1]:
                top = row + 1 
            else:
                break

        l = 0 
        r = len(matrix[0]) - 1
        while l <= r:
            m = (r + l) // 2 
            if matrix[row][m] == target:
                return True 
            elif matrix[row][m] > target:
                r = m - 1 
            else:
                l = m + 1 

        return False 