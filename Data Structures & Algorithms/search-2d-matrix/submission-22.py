class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bot = 0 , len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2 
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1 
            else:
                break

        else:
            return False 

        l , r = 0 , len(matrix[0]) - 1 
        while l <= r:
            m = (l + r) // 2 
            e = matrix[row][m]
            if e == target:
                return True
            elif e > target:
                r = m - 1 
            else:
                l = m + 1 
        return False 