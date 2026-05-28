class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l , r = 1 , max(piles)
        while l <= r:
            k = (l + r) // 2 
            rate = 0 
            for p in piles:
                rate += int(math.ceil(p / k))
            if rate <= h:
                ans = min(ans , k)
                r = k - 1 
            else:
                l = k + 1 


        return ans 