"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [ s.start for s in intervals]
        end = [s.end for s in intervals]
        start.sort()
        end.sort()
        count = 0 
        res = 0 
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1 
                s += 1
            else:
                count -= 1 
                e += 1

            res = max(res , count)

        return res 