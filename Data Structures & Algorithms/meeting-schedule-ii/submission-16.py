"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0 
        start = []
        end = []
        
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s , e , = 0 , 0 
        cur = 0 
        while s < len(start):
            if start[s] < end[e]:
                cur += 1
                s += 1
            else:
                cur -= 1 
                e += 1 
            rooms = max(rooms , cur)

        return rooms
            