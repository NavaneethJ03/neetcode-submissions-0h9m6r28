class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 
        l , r = 0 , len(height) - 1 
        maxLeft , maxRight = height[l] , height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1 
                trap = maxLeft - height[l]
                if trap > 0:
                    ans += trap 

                maxLeft = max(maxLeft , height[l])
            else:
                r -= 1 
                trap = maxRight - height[r]
                if trap > 0:
                    ans += trap 
                maxRight = max(maxRight , height[r])

        return ans 