class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        res = []
        res.append(intervals[0])
        lastend = intervals[0][1]
        for i in range(1,  len(intervals)):
            if intervals[i][0] <= lastend:
                res[-1][1] = max(intervals[i][1] , lastend)

            else:
                res.append(intervals[i])

            lastend = res[-1][1]

        return res