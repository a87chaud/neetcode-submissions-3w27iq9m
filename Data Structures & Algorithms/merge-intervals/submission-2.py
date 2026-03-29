class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            # print(f'interval: {interval} result: {result}')
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][0] = min(interval[0], result[-1][0])
                result[-1][1] = max(interval[1], result[-1][1])
        return result