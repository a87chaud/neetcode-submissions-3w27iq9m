class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeStack = []
        posAndSpeed = zip(position, speed)
        posAndSpeedSorted = sorted(posAndSpeed, key=lambda x: x[0], reverse=True)
        for pos, sp in posAndSpeedSorted:
            time = (target - pos) / sp
            if not timeStack:
                timeStack.append(time)
            elif time > timeStack[-1]:
                timeStack.append(time)
        return len(timeStack)