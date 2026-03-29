class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyMap:
            self.keyMap[key].append((value, timestamp))
        else:
            self.keyMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
        
        possibleKeys = self.keyMap[key]
        print(possibleKeys)
        l, r= 0, len(possibleKeys) - 1
        if possibleKeys[l][1] > timestamp:
            return ""
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if possibleKeys[mid][1] <= timestamp:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return possibleKeys[res][0]