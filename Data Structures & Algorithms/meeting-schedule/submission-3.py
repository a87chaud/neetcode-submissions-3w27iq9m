"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        stack = []
        for interval in intervals:
            if stack and stack[-1].end > interval.start:
                return False
            stack.append(interval)
        return True