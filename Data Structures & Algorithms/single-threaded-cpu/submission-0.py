class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        [[2,10], [3,3], [4,1], [4,4], [5,2]]
        t=2
        --------------------|12
                            -------------
        '''
        minHeap = []
        for i,(start, duration) in enumerate(tasks):
            heapq.heappush(minHeap, (start, duration, i))
        # print(minHeap)
        nextAvailTime = 0 # might have to set to the first element of heap
        order = []
        queue = []
        while minHeap or queue:
            if not queue and nextAvailTime < minHeap[0][0]:
                nextAvailTime = minHeap[0][0]
            
            while minHeap and minHeap[0][0] <= nextAvailTime:
                start, end, idx = heapq.heappop(minHeap)
                heapq.heappush(queue, (end,idx))
            
            if queue:
                dur, idx = heapq.heappop(queue)
                order.append(idx)
                nextAvailTime += dur

        return order

