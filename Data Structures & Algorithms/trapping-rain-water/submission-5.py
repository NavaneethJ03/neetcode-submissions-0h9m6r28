class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0 
        left , right = 0 , n - 1 
        maxLeft , maxRight = height[left] , height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1 
                trap = maxLeft - height[left]
                if trap > 0:
                    ans += trap

                maxLeft = max(maxLeft , height[left])
            else:
                right -= 1 
                trap = maxRight - height[right]
                if trap > 0:
                    ans += trap 

                maxRight = max(maxRight , height[right])

        return ans
        