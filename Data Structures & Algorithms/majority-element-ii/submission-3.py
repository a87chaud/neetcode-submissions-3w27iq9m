class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1
        print(freqMap)
        res = []
        for num, freq in freqMap.items():
            if freq > len(nums) // 3:
                res.append(num)
        return res