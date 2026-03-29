class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = 0

        for s2 in range(len(t)):
            if s1 >= len(s):
                return True
            if t[s2] == s[s1]:
                s1 += 1
        return s1 == len(s)