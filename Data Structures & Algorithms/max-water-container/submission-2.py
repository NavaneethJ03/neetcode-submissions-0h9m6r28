class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ans = 0 
        l , r = 0 , len(heights) - 1 

        while l < r:
            store = (r - l) * min(heights[l] , heights[r])
            ans = max(ans , store)
            if heights[l] > heights[r]:
                r -= 1 
            else:
                l += 1 

        return ans 