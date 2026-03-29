class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {len(s): True}
        def dfs(index: int):
            if index == len(s):
                return True
            if index in cache:
                return cache[index]
            for w in wordDict:
                if s[index: index + len(w)] == w:
                    if dfs(index + len(w)):
                        cache[index] = True
                        return True
            cache[index] = False
            return False
        
        return dfs(0)