class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)

        for i in range(len(s2)):
            currWindow = s2[i:i+windowSize]
            if sorted(currWindow)== sorted(s1):
                return True
        return False