class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            res = 0
            while n != 0:
                rem = n % 10
                res += rem * rem
                n = n // 10 
            return res

        visit = set()
        while n != 1:
            n = sumSquares(n)
            if n in visit:
                return False 
            visit.add(n)

        return True