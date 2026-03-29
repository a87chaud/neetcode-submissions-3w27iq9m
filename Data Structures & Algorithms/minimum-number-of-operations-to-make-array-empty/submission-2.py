class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        
        ops = 0
        for num, freq in freqMap.items():
            if freq == 1:
                return -1
            if freq % 3 == 0:
                ops += freq // 3
            elif freq % 3 == 1:
                # ops += (freq) // 3 + 1
                if freq // 3 - 1 > 0:
                    totalThree = freq // 3 - 1
                else:
                    totalThree = 0
                # print(totalThree *)
                ops += totalThree
                ops += (freq - totalThree * 3) // 2
            elif freq % 3 == 2:
                ops += (freq // 3) + 1
        print(freqMap)
        # print(ops)
        return ops
        
