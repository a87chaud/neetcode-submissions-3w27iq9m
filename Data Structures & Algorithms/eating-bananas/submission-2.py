class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            # check if mid is the right eating rate
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours > h:
                l = mid + 1
            
            if hours <= h:
                res = mid
                r = mid - 1
            
        return res