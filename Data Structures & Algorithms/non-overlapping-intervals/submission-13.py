class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        lastEnd = intervals[0][1]
        ans = 0
        for start , end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end 
            else:
                ans += 1 
                lastEnd = min(end , lastEnd)

        return ans