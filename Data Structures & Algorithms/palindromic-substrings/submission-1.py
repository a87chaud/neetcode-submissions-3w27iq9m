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
        self.res = 0
        visited = set()
        def backtrack(start: int, end: int):
            if start > end or (start, end) in visited:
                return
            visited.add((start, end))
            curr = s[start:end + 1]
            if self.isPalindrome(curr):
                print(f'curr: {curr} res: {self.res}')
                self.res += 1
            
            backtrack(start, end - 1)
            backtrack(start + 1, end)
        
        backtrack(0, len(s) - 1)
        return self.res
    