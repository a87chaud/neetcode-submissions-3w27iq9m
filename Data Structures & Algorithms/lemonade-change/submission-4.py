class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billMap = defaultdict(int)
        for b in bills:
            if not billMap and b > 5:
                return False
            change = b - 5
            billMap[b] += 1
            if change == 5:
                billMap[5] -= 1
                if billMap[5] < 0:
                    return False
            elif change == 15:
                if billMap[10] > 0 and billMap[5] > 0:
                    billMap[10] -= 1
                    billMap[5] -= 1
                
                elif billMap[10] == 0 and billMap[5] >= 3:
                    billMap[5] -= 3
                else:
                    return False
        return True