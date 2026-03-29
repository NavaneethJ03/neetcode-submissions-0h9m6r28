class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the range is going to be btw 1 and the max of piles
        l , r = 1 , max(piles)
        res = r 

        while l <= r:
            totalTime = 0 
            k = (l + r) // 2 
            for p in piles:
                totalTime += math.ceil(p / k) # we take ceil value since we cannot eat extra 
            
            if totalTime <= h:
                res = k 
                r = k - 1 
            else:
                l = k + 1 
        return res 
