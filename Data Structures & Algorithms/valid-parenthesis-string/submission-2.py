class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        for i, c in enumerate(s):
            if c == ')' and len(openStack) == 0 and len(starStack) == 0:
                return False
            if c == "*":
                starStack.append(i)
            elif c == '(':
                openStack.append(i)
            elif c == ')' and openStack:
                openStack.pop()
            elif c == ')' and starStack:
                starStack.pop()
        print(openStack)
        print(starStack)
        while openStack and starStack:
            currOpen = openStack.pop()
            currStar = starStack.pop()

            if currOpen > currStar:
                return False
        return True if len(openStack) <= len(starStack) else False