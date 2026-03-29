class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bottom = 0  , len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1 
            elif target > matrix[row][-1]:
                top = row + 1

            else:
                break

        if not (top <= bottom):
            return False 
            
        l , r = 0 , len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True  

            elif target < matrix[row][mid]:
                r = mid - 1

            else:
                l = mid + 1 


        return False 