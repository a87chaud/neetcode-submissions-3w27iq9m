class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        return max(freq, key=freq.get)