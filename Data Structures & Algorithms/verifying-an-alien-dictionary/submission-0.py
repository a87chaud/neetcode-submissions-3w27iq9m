class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        
        word1 = words[0]

        for w in range(1, len(words)):
            word1, word2 = words[w-1], words[w]
            ####
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if orderMap[word1[j]] > orderMap[word2[j]]:
                        return False
                    break
            ####
            word1 = word2
        
        return True
