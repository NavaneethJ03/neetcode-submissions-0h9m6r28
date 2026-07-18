class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n 
        
        one , two = 1 , 2 

        for _ in range(2 , n):
            one , two = two , one + two

        return two
        