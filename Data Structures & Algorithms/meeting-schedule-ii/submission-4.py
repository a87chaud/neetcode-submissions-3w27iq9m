"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = [interval.start for interval in intervals]
        startTimes.sort()
        endTimes = [interval.end for interval in intervals]
        endTimes.sort()
        s, e = 0, 0
        numMeetings = 0
        res = 0
        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                s += 1
                numMeetings += 1
            else:
                e += 1
                numMeetings -= 1
            res = max(numMeetings, res)
        return res


