class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l , r = 0 , len(height) - 1
        maxleft = height[l]
        maxright = height[r] 

        while l < r:
            if maxleft < maxright:
                l += 1 
                trap = maxleft - height[l]
                if trap > 0:
                    ans += trap
                maxleft = max(maxleft , height[l])

            else:
                r -= 1 
                trap = maxright - height[r]
                if trap > 0:
                    ans += trap 
                maxright = max(maxright , height[r])

        return ans