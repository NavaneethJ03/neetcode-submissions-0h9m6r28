class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            s , e = intervals[i][0] , intervals[i][1]
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > e:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0] , s) , max(newInterval[1] , e)]
        res.append(newInterval)
        return res
