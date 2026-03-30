class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True 

        return False 

    def sumOfSquares(self , n):
        res = 0
        while n > 0:
            digit = n % 10 
            sq = digit ** 2 
            res += sq
            n //= 10 

        return res 
            