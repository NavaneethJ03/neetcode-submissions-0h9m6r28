class Solution:
    def maxArea(self, h: List[int]) -> int:
        ans = 0 
        l , r = 0 , len(h) - 1 
        while l < r :
            area = (r - l) * min(h[l] , h[r])
            ans = max(ans,area)
            if h[l] >= h[r]:
                r -= 1 
            else:
                l += 1 

        return ans 