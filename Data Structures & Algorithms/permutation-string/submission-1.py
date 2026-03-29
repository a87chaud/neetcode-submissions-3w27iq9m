class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Sorted = sorted(s1)
        
        windowSize = len(s1)

        for r in range(len(s2) - windowSize + 1):
            if sorted(s2[r: r + windowSize]) == s1Sorted:
                return True
        return False