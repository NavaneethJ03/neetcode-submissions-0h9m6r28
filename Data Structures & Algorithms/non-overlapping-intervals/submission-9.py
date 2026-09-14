class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0 
        intervals.sort(key = lambda x : x[0])

        lastEnd = intervals[0][1]

        for start , end in intervals[1:]:
            if start < lastEnd:
                ans += 1 
                lastEnd = min(lastEnd , end)
            else:
                lastEnd = end

        return ans