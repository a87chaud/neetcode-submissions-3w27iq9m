class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(sorted_freq)
        return [sorted_freq[x][0] for x in range(0, k)]