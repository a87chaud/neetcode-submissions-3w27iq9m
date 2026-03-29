class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if y < x:
                heapq.heappush(maxHeap, -1 * (x - y))
            
        return -1 * maxHeap[0] if maxHeap else 0