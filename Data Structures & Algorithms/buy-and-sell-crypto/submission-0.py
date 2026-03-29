class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buyIndex = 0

        for sellIndex in range(1, len(prices)):
            currProfit = prices[sellIndex] - prices[buyIndex]
            # print(f'b: {buyIndex} s: {sellIndex} profit: {currProfit}')
            if currProfit < 0:
                buyIndex = sellIndex
            result = max(currProfit, result)
        return result