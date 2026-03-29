class Node:
    def __init__(self, char: str):
        self.char = char
        self.word = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.word = True
    def search(self, word: str) -> bool:
        def dfs(index: int, curr: Node) -> bool:
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for val in curr.children.values():
                        if dfs(i + 1, val):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.word
        return dfs(0, self.root)
