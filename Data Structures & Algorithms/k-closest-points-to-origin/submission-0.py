class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for p in points:
            dist = (p[0] ** 2 + p[1] ** 2) ** 0.5
            maxHeap.append((-dist, p))
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        return [p for dist, p in maxHeap]