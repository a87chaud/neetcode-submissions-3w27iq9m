class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        a = 0
        b = 1
        c = 3

        cc
        '''
        res = []
        maxHeap = []
        if a > 0:
            maxHeap.append((-a, 'a'))
        if b > 0:   
            maxHeap.append((-b, 'b'))
        if c > 0:
            maxHeap.append((-c, 'c'))
        
        heapq.heapify(maxHeap)

        while maxHeap:
            maxFreq, maxElement = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == maxElement and maxHeap:
                second, secondElement = heapq.heappop(maxHeap)
                res.append(secondElement)
                heapq.heappush(maxHeap, (maxFreq, maxElement))
                if second + 1 < 0:
                    heapq.heappush(maxHeap, (second+1, secondElement))
            elif len(res) >= 3 and res[-1] == res[-2] == maxElement and len(maxHeap) < 1:
                break
            else:
                res.append(maxElement)
                if maxFreq + 1 < 0:
                    heapq.heappush(maxHeap, (maxFreq + 1, maxElement))
        return ''.join(res)