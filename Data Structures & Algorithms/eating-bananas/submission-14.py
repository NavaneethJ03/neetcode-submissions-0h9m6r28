class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l = 1 
        r = max(piles)

        while l < r:
            m = (l + r) // 2 
            time = 0
            for p in piles:
                time += math.ceil(p / m)

            if time <= h:
                ans = min(ans , m)
                r = m

            else:
                l = m + 1 

        return ans