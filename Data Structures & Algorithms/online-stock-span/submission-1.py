class StockSpanner:

    def __init__(self):
        self.stack = [] # push (price, span)

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
            return 1
        totalSpan = 1
        while self.stack and self.stack[-1][0] <= price:
            oldPrice, oldSpan = self.stack.pop()
            totalSpan += oldSpan
        self.stack.append((price, totalSpan))
        return totalSpan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)