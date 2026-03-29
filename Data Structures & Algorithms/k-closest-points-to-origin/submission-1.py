class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            dist = (p[0] ** 2 + p[1] ** 2) ** 0.5
            minHeap.append((dist, p))
        
        heapq.heapify(minHeap)
        result = []
        while k > 0:
            minDist, minPoint = heapq.heappop(minHeap)
            result.append(minPoint)
            k -= 1
        
        return result