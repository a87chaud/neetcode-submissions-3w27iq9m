class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def build() -> str:
            nonlocal i
            result = ''
            multiply = ''
            currNum = ''
            while i < len(s):
                while s[i].isdigit():
                    currNum += s[i]
                    i += 1
                print(currNum)
                if s[i] == '[':
                    i += 1
                    if currNum:
                        result += int(currNum) * build()
                    currNum = ''
                elif s[i] == ']':
                    return result
                else:
                    result += s[i]
                i += 1
            return result
        return build()