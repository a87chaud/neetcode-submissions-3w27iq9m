class Node:
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        level = self.root
        for i, c in enumerate(word):
            if c not in level:
                level[c] = Node(c)
            if i < len(word) - 1:
                level = level[c].children

        level[c].isWord = True
    def search(self, word: str) -> bool:
        level = self.root
        for i, c in enumerate(word):
            if c not in level:
                return False
            if i < len(word) - 1:
                level = level[c].children
        return level[c].isWord

    def startsWith(self, prefix: str) -> bool:
        level = self.root
        for i, c in enumerate(prefix):
            if c not in level:
                return False
            level = level[c].children
        return True
        