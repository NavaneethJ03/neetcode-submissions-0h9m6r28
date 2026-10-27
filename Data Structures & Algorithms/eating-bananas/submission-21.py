class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)

        def canEat(time):
            eat = 0
            for p in piles:
                eat += math.ceil(p / time)

            if eat <= h:
                return True
            return False 

        while l < r:
            m = (l + r) // 2
            if canEat(m):
                r = m
            else:
                l = m + 1 

        return l