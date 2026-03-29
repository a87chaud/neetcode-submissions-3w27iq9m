class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        currSet = set()
        freqMap = defaultdict(int)

        for c in s:
            freqMap[c] += 1
        length = 0
        currSet.add(s[0])
        for c in s: 
            if c in currSet:
                length += 1
                freqMap[c] -= 1
                if freqMap[c] <= 0:
                    del freqMap[c]
            elif c not in currSet and any(x in freqMap for x in currSet):
                length += 1
                currSet.add(c)
                freqMap[c] -= 1
                if freqMap[c] <= 0:
                    del freqMap[c]
            else:
                result.append(length)
                length = 1
                currSet.clear()
                currSet.add(c)
                freqMap[c] -= 1
                if freqMap[c] <= 0:
                    del freqMap[c]
        result.append(length)
        return result