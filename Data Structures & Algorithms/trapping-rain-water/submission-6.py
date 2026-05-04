class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l , r = 0 , n - 1 
        maxLeft = height[l]
        maxRight = height[r]
        res = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1 
                trap = maxLeft - height[l]
                if trap > 0:
                    res += trap
                maxLeft = max(maxLeft , height[l])

            else:
                r -= 1 
                trap = maxRight - height[r]
                if trap > 0:
                    res += trap 
                maxRight = max(maxRight , height[r])

        return res 
