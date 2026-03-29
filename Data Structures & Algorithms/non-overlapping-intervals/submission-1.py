class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        stack = []
        counter = 0

        for interval in intervals:
            if not stack or stack[-1][1] <= interval[0]:
                stack.append(interval)
            else:
                counter += 1
        return counter