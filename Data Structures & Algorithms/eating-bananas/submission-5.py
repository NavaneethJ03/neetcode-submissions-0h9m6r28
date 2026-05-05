class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l , r = 1 , max(piles)
        while l <= r:
            rate = 0
            k = (l + r) // 2 
            for p in piles:
                rate += int(math.ceil(p / k))
            if rate <= h:
                ans = k
                r = k - 1 
            elif rate > h:
                l = k + 1 
                
        return ans