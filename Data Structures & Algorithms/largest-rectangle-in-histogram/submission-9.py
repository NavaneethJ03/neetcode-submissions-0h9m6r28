class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stk = []

        for i , h in enumerate(heights):
            startidx = i    

            while stk and h < stk[-1][1]:
                index , height = stk.pop()
                ans = max(ans , height * (i - index))
                startidx = index 

            stk.append([startidx , h])

        for i , h in stk:
            ans = max(ans , h * (len(heights) - i ))


        return ans