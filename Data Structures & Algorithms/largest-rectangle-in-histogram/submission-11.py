class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        ans = 0 

        for i , h in enumerate(heights):
            start = i
            while stk and h < stk[-1][1]:
                idx , height = stk.pop()
                area = height * (i - idx)
                ans = max(area , ans)
                start = idx

            stk.append([start , h])

        for i , h in stk:
            area = h * (len(heights) - i)
            ans = max(ans , area)

        return ans