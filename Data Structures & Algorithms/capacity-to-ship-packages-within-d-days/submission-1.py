class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # need to find a capacity between max(weights), 500
        l, r = max(weights), 50000

        while l <= r:
            mid = (l + r) // 2
            # mid represents max weight
            totalDays = 1
            currCap = 0
            print(mid)
            for w in weights:
                # print(f'w: {w} days: {totalDays} cap: {currCap}')
                currCap += w
                if currCap > mid:
                    currCap = w
                    totalDays += 1
            # print(f'days: {totalDays} mid: {mid}')
            if totalDays <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l
            