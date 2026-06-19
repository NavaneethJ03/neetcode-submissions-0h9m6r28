class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        i = 1 
        res = [intervals[0]]
        lastEnd = intervals[0][1]
        while i < len(intervals):
            lastEnd = res[-1][1]
            if intervals[i][0] <= lastEnd:
                res[-1][1] = max(lastEnd , intervals[i][1])
                
            else:
                res.append(intervals[i])

            i += 1 

        return res 