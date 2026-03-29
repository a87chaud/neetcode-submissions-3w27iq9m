class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            mid = (l + r) // 2
            print(f'x: {x} mid: {mid}')
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
                res = l
            else:
                r = mid - 1
        return res - 1