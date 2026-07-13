class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l , r = 1 , max(piles)

        while l < r:
            k = (l + r) // 2 
            total = 0 
            for p in piles:
                total += math.ceil(p / k)
                
            if total <= h:
                ans = k
                r = k 
            elif total > h:
                l = k + 1 

        return ans
