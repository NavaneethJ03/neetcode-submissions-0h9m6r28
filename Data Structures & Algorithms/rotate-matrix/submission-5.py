class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix) , len(matrix[0])

        top , bottom = 0 , rows - 1 
        left , right = 0 , cols - 1

        while top < bottom:
            for i in range(right - left):
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft
            top += 1 
            bottom -= 1 
            left += 1 
            right -= 1 

            