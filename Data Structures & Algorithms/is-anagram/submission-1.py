class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        for c in t:
            currIndex = ord(c) - ord('a')
            counts[currIndex] -= 1

        return all(x == 0 for x in counts)