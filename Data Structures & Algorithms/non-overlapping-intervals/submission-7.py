class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        count = 0 

        lastEnd = intervals[0][1]

        for s , e in intervals[1:]:
            if s < lastEnd:
                lastEnd = min(lastEnd , e)
                count += 1 
            else:
                lastEnd = e

            
        return count 