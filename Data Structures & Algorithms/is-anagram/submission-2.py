class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = [0] * 26

        for c in s:
            charCount[ord(c) - ord('a')] += 1
        
        for c in t:
            charCount[ord(c) - ord('a')] -= 1
        
        return all(x == 0 for x in charCount)