class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        visited = set()
        for i in range(len(s)):
            # odd -> l,r is the middle
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(f'l odd: {l} r odd: {r}')
                l -= 1
                r += 1
                total += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(f'l even: {l} r even: {r}')
                l -= 1
                r += 1
                total += 1
        return total