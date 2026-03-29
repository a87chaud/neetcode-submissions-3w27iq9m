class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prev = {}
        def dfs(rem: int):
            if rem == 0:
                return 0
            if rem in prev:
                return prev[rem]
            res = float('inf')

            for c in coins:
                if rem - c >= 0:
                    numCoins = 1 + dfs(rem - c)
                    res = min(numCoins, res)
            prev[rem] = res
            return res
        t = dfs(amount)
        return t if t != float('inf') else -1