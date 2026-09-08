class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l , r = 1 , max(piles)

        while l < r:
            m = (l + r) // 2 
            time = 0 
            for p in piles:
                time += math.ceil(p / m)

            if time <= h:
                ans = m 
                r = m 
            else:
                l = m + 1 

        return ans
