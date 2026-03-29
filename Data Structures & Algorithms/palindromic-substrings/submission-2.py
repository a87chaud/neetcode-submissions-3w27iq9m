class Solution:
    def isPalindrome(self, s: List[str]) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    res += 1
        return res