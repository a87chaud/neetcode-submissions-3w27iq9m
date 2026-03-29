class Solution:
    def climbStairs(self, n: int) -> int:
        last, secondLast = 1, 1
        curr = last
        for i in range(n - 2, -1, -1):
            curr = last + secondLast
            last = secondLast
            secondLast = curr
        return curr