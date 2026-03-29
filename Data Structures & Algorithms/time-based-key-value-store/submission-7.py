class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        if not arr:
            return ''
        l, r = 0, len(arr) - 1
        res = ''
        while l <= r:
            mid = (l + r) // 2
            print(f'ts: {timestamp} l: {l} r: {r} mid: {mid}')
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
