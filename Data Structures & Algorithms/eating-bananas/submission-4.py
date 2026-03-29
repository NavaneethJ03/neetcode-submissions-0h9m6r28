class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        ans = max(piles)
        while l <= r:
            rate = 0 
            k = (l + r) // 2 
            for p in piles:
                rate += math.ceil(p / k)
            if rate > h:
                l = k + 1 
            else:
                ans = k
                r = k - 1
                
        return ans 
