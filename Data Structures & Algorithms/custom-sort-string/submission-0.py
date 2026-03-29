class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sFreqMap = Counter(s)
        result = []
        for i in range(len(order)):
            if order[i] in sFreqMap:
                result.extend([order[i]] * sFreqMap[order[i]])
                del sFreqMap[order[i]]
        for key, val in sFreqMap.items():
            a = [key] * val
            result.extend(a)       
        return ''.join(result)