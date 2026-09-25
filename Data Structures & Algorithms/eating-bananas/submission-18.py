class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)

        while l < r:
            time = 0 
            m = (l + r) // 2 
            for p in piles:
                time += math.ceil(p / m)
            if time > h:
                l = m + 1 
            else:
                r = m 
        return l