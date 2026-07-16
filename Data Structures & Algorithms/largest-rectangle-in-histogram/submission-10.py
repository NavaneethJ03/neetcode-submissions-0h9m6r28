class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        ans = 0 

        for i , h in enumerate(heights):
            start = i
            while stk and h < stk[-1][1]:
                idx , height = stk.pop()
                ans = max(ans , height * (i - idx))
                start = idx
            stk.append([start , h])

        for i , h in stk:
            ans = max(ans , h * (len(heights) - i))

        return ans