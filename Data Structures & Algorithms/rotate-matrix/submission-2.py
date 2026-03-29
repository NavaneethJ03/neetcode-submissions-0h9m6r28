class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top , bottom = 0 , len(matrix) - 1

        while top < bottom:
            l , r = top , bottom
            for i in range(r - l):
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft

            top += 1 
            bottom -= 1 

    
