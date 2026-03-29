class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends or target in deadends:
            return -1
        queue = deque([("0000", 0)])

        def children(lock):
            res = []
            for i in range(4):
                digit = (int(curr[i]) + 1) % 10
                res.append(curr[:i] + str(digit) + curr[i+1:])
                digit = (int(curr[i]) - 1 + 10) % 10
                res.append(curr[:i] + str(digit) + curr[i+1:])
            return res
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            for c in children(curr):
                if c not in deadends:
                    queue.append((c, steps + 1))
                    deadends.add(c)
        return -1
             