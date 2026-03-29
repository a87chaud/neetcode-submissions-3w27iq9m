class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums))]
        for n in nums:
            freq[n] += 1
        
        for number, occurrence in freq.items():
            buckets[occurrence - 1].append(number)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            curr = buckets[i]
            for number in curr:
                if len(res) >= k:
                    return res
                res.append(number)
        return res
        