class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0 # pointer for t
        prefix = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                prefix += 1
                j += 1
        
        return len(t) - prefix