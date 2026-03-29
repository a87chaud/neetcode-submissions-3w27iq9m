class Solution:
    def isPalindrome(self, s: List[str]) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []
        def backtrack(index: int):
            if index == len(s):
                result.append(temp.copy())
                return
            for i in range(index, len(s)):
                if self.isPalindrome(s[index: i + 1]):
                    temp.append(s[index: i + 1])
                    backtrack(i + 1)
                    temp.pop()

            return
        
        backtrack(0)
        return result