class RandomizedSet:

    def __init__(self):
        self.valMap = {} # val -> index
        self.valList = []

    def insert(self, val: int) -> bool:
        if val in self.valMap:
            return False
        self.valList.append(val)
        self.valMap[val] = len(self.valList) - 1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.valMap:
            return False
        removeIndex = self.valMap[val]
        # swap with last element + pop
        last = self.valList[-1]
        self.valList[removeIndex] = last
        self.valList.pop()
        self.valMap[last] = removeIndex
        del self.valMap[val]
        return True
    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.valList) - 1)
        return self.valList[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()