class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for currStr in strs:
            sortedStr = sorted(currStr)
            lol = ''.join(sortedStr)
            anagramMap[lol].append(currStr)
        return [val for val in anagramMap.values()]