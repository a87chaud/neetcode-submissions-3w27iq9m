class MyQueue:

    def __init__(self):
        self.stack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        if self.popStack:
            return self.popStack.pop()
        # copy all element from stack
        while self.stack:
            self.popStack.append(self.stack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        if self.popStack:
            return self.popStack[-1]
        while self.stack:
            self.popStack.append(self.stack.pop())
        return self.popStack[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.popStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()