class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {len(s): True}
        def dfs(index: int):
            if index == len(s):
                return True
            print(cache)
            if index in cache:
                return cache[index]
            for i in range(index, len(s)):
                if s[index: i + 1] in wordSet:
                    if dfs(i + 1):
                        cache[index] = True
                        return True
            cache[index] = False
            return False
        
        return dfs(0)