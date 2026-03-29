class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for r in range(len(arr)):
            diff = abs(x - arr[r])
            heapq.heappush(heap, (-diff, -arr[r]))
            # print(heap)
            while len(heap) > k:
                heapq.heappop(heap)
        res = [-x[1] for x in heap]
        res.sort()
        return res