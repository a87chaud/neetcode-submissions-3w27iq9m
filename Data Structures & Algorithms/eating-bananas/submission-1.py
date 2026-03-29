class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1
        res = 0
        while l < r:
            mid = (l + r) // 2
            currHours = 0
            for p in piles:
                currHours += math.ceil(p / mid)
            
            if currHours <= h:
                res = mid
                r = mid
            else:
                l = mid + 1
        return res