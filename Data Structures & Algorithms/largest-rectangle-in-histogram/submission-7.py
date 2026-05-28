class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stk = [] # we are going to store both the height and the start idx

        for i , h in enumerate(heights):
            startidx = i
            while stk and h < stk[-1][1]:
                idx , height = stk.pop()
                ans = max(ans , height * (i - idx))
                startidx = idx 

            stk.append([startidx , h])

        for i , h in stk:
            ans = max(ans , h * (len(heights) - i))

        return ans 