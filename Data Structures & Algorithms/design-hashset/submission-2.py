class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        idx = key % 1000
        if key in self.hashset[idx]:
            return
        self.hashset[idx].append(key) # O(1)

    def remove(self, key: int) -> None:
        idx = key % 1000
        if key not in self.hashset[idx]:
            return
        self.hashset[idx].remove(key) # O(n)

    def contains(self, key: int) -> bool:
        idx = key % 1000
        return any(x == key for x in self.hashset[idx])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)