class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Freq = Counter(s1)
        windowSize = len(s1)
        windowFreq = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            windowFreq[s2[r]] += 1
            if (r - l + 1) > windowSize:
                windowFreq[s2[l]] -= 1
                if windowFreq[s2[l]] <= 0:
                    del windowFreq[s2[l]]
                l += 1

            if windowFreq == s1Freq:
                return True
        return False