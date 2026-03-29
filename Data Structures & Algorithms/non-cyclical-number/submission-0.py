class Solution:
    def isHappy(self, n: int) -> bool:
        self.seen = set()
        t = n
        while self.sumofDigit(t) != 1:
            t = self.sumofDigit(t)
            if t in self.seen:
                return False 
            self.seen.add(t)

        return True 

    def sumofDigit(self , n):
        ans = 0 
        while n:
            ans += (n % 10) ** 2 
            n //= 10 

        return ans 
             
        
