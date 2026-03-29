class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0
        for i , h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][0]:
                height , idx = stack.pop()
                maxArea = max(maxArea , (height * (i - idx)))
                start = idx
            stack.append((h , start))

        for h , idx in stack:
            maxArea = max(maxArea , (h * (n - idx)))

        return maxArea 

