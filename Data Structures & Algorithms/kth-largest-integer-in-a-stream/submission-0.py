class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k
    
    def findKthLargest(self):
        curr = self.k
        tempHeap = self.heap.copy()
        while curr > 0:
            maxElement = heapq.heappop(tempHeap)
            curr -= 1
        return -1 * maxElement
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        return self.findKthLargest()