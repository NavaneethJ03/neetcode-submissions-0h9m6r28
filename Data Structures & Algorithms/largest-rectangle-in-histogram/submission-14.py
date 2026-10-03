class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stk = []

        for i , h in enumerate(heights):
            startIdx = i
            while stk and h < stk[-1][1]:
                idx , height = stk.pop()
                ans = max(ans , height * (i - idx))
                startIdx = idx
            stk.append([startIdx , h])

        for i , h in stk:
            ans = max(ans , (len(heights) - i) * h)

        return ans