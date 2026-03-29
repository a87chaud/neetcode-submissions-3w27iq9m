class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Freq = Counter(s1)
        windowSize = len(s1)

        for i in range(len(s2)):
            window = s2[i:i+windowSize]
            if Counter(window) == s1Freq:
                return True
        return False