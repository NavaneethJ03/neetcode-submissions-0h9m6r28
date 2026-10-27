class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stk = []

        for i , h in enumerate(heights):
            startIdx = i
            while stk and h < stk[-1][1]:
                idx , height = stk.pop()
                area = (i - idx) * height
                ans = max(ans, area)
                startIdx = idx
            stk.append([startIdx , h])

        for i , h in stk:
            area = (len(heights) - i) * h
            ans = max(ans , area)

        return ans