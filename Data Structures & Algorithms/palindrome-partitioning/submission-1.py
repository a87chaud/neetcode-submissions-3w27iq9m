class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        def backtrack(index: int):
            if index == len(s):
                res.append(path.copy())
                return
            
            for i in range(index, len(s)):
                curr = s[index: i + 1]
                if self.isPalindrome(curr):
                    path.append(curr)
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        return res