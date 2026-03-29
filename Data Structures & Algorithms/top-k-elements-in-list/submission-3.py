class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            while len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]

        