class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        intervals.sort(key = lambda x : x[0])
        lastEnd = intervals[0][1]
        for i in range(1 , len(intervals)):
            if intervals[i][0] < lastEnd:
                count += 1 
                lastEnd = min(lastEnd , intervals[i][1])
            else:
                lastEnd = intervals[i][1]
        return count