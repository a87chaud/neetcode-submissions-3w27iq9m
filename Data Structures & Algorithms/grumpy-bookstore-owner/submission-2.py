class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        windowStart = 0
        l = 0
        maxDiff = 0
        numCustomers = 0
        numCustomersGrumpy = 0
        for r in range(len(customers)):
            numCustomers += customers[r] # total customers
            numCustomersGrumpy += customers[r] if not grumpy[r] else 0
            if (r - l + 1) == minutes:
                # want to see if 
                currDiff = numCustomers - numCustomersGrumpy
                if currDiff >= maxDiff:
                    windowStart = l
                maxDiff = max(maxDiff, currDiff)
                numCustomers -= customers[l]
                numCustomersGrumpy -= customers[l] if not grumpy[l] else 0
                l += 1

            # print(f'l: {l} r: {r} numCustomers: {numCustomers}')
        # print(f'max customers: {maxCustomers} windowStart: {windowStart}')
        total = 0
        for i in range(len(customers)):
            if windowStart <= i <= windowStart + minutes - 1:
                total += customers[i]
            elif not grumpy[i]:
                total += customers[i]
        return total