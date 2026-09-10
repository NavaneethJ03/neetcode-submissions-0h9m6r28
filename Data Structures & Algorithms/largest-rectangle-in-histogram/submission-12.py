class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        area = 0 

        for i , h in enumerate(heights):
            startIdx = i
            while stk and stk[-1][1] > h:
                idx , prevHeight = stk.pop()
                area = max(area , prevHeight * (i - idx))
                startIdx = idx
            stk.append([startIdx , h])

        for idx , h in stk:
            area = max(area , h * (len(heights) - idx))

        return area