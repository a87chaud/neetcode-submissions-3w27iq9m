class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        1. What is the problem asking
        we have n cars and we want to find position of each car at time i 
        t = 4
        i = 0       i = 1   i = 2
        c1 = 0      c1 = 3  c1 = 6
        c2 = 2      c2 = 6 // reached
        c3 = 1      c3 = 3  c3 = 4
        '''
        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []
        for pos, spd, in pairs:
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
