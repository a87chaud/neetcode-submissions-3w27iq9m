class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {c: i for i, c in enumerate(s)}
        end = 0
        result = []
        start = 0
        for i, c in enumerate(s):
            end = max(end, lastOcc[c])

            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result