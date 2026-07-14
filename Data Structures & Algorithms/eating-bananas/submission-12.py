class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l , r = 1 , max(piles)
        while l < r:
            m = (l + r) // 2 
            k = 0 
            for p in piles:
                k += math.ceil(p / m)
            
            if k <= h:
                ans = m
                r = m 
            elif k > h:
                l = m + 1 

        return ans