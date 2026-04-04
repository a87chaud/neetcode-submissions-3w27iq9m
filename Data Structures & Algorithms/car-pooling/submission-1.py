class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        {
            1: 2
            3: -2
            2: 3
            4:
        }
        # check if start point in passengers: add num pass
        # check if end point in passengers: sub num pass
        '''
        trip_map = defaultdict(int)

        for num_pass, start, end in trips:
            trip_map[start] += num_pass
            trip_map[end] -= num_pass
        
        minHeap = list(trip_map.keys())
        heapq.heapify(minHeap)
        total = 0
        while minHeap:
            curr = heapq.heappop(minHeap)
            total += trip_map[curr]
            if total > capacity:
                return False
        return True