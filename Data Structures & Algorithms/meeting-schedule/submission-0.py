"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        n = len(intervals)
        for i in range(n - 1):
            lastEnd = intervals[i].end
            start , end = intervals[i+1].start , intervals[i+1].end
            if lastEnd > start:
                return False 

            lastEnd = end 

        return True
