class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] <= newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1
        intervals.insert(l, newInterval)
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
        return result
