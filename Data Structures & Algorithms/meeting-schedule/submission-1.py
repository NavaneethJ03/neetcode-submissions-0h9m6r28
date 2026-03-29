"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # meetings = [[intervals[i].start , intervals[i].end] for i in range(intervals)]
        intervals.sort(key = lambda x : x.start)
        for i in range(len(intervals) - 1):
            lastEnd = intervals[i].end
            start , end = intervals[i+1].start , intervals[i+1].end
            if start < lastEnd:
                return False 
            lastEnd = max(end , lastEnd)

        return True