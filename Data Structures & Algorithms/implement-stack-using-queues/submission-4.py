class MyStack:

    def __init__(self):
        self.q1 = deque([])
    def push(self, x: int) -> None:
        swap = x
        length = len(self.q1)
        for _ in range(length):
            # pop then append
            old = self.q1.popleft()
            self.q1.append(swap)
            swap = old
        self.q1.append(swap)
        print(self.q1)
    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()