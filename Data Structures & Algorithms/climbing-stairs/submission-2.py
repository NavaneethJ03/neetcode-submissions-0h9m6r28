class Solution:
    def climbStairs(self, n: int) -> int:
        one  , two  =  1 , 1 
        for _ in range(1 , n):
            one , two = two , two + one 

        return two