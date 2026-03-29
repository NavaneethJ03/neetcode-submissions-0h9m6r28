class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0 
        intervals.sort()
        lastEnd = intervals[0][1]
        
        for start , end in intervals[1:]:
            if start < lastEnd:
                ans += 1
                lastEnd = min(end , lastEnd)

            else:
                lastEnd = end

        return ans 

