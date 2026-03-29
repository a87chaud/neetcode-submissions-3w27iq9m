class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        buckets = [[]  for _ in range(len(nums))]
        for n in nums:
            numMap[n] += 1
        
        for key, val in numMap.items():
            # print(val)
            buckets[val - 1].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            curr = buckets[i]
            j = 0
            while j < len(curr) and len(res) < k:
                res.append(curr[j])
                j += 1
        return res