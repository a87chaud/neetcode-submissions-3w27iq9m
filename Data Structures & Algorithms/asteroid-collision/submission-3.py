class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        destroyed = False

        for a in asteroids:
            destroyed = False
            # collision
            while stack and a < 0 and stack[-1] > 0:
                if abs(stack[-1]) == abs(a):
                    # mutual destruction
                    stack.pop()
                    destroyed = True
                    break
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                else:
                    destroyed = True
                    break
            if not destroyed:
                stack.append(a)
        return stack