class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)
        for t in tasks:
            freqMap[t] += 1
        
        maxHeap = [-val for val in freqMap.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque([])

        while maxHeap or queue:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1
                if freq < 0:
                    queue.append((freq, time + n))
            if queue and queue[0][1] == time:
                qFreq, qTime = queue.popleft()
                heapq.heappush(maxHeap, qFreq)
        return time