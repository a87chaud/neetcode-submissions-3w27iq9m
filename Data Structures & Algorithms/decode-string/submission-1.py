class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            elif c == ']':
                curr = []
                num = []
                while stack and stack[-1] != '[':
                    curr.append(stack.pop())
                # this should be the open bracket
                if stack and stack[-1] == '[':
                    stack.pop()
                
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                curr.reverse()
                finalNum = int(''.join(num))
                finalString = ''.join(curr) * finalNum
                print(f'num: {finalNum} finalString: {finalString}')
                stack.append(finalString)
        return ''.join(stack)