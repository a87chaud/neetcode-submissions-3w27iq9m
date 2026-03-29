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
            if not stack or stack[-1].end <= interval.start:
                stack.append(interval)
            else:
                return False
        return True