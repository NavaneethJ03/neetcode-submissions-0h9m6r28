class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        top , bot = 0 , len(matrix) - 1 

        while top < bot:
            l , r = top , bot
            for i in range(r - l):
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bot - i][l]
                matrix[bot - i][l] = matrix[bot][r - i]
                matrix[bot][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft 
            top += 1 
            bot -= 1 

        