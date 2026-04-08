class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        {a: 0, b: 0 c: 0 d: 0}
        curr element = c

        d   b   c   a   d   c
        '''
        freqMap = Counter(s)
        maxHeap = [(-val, key) for key,val in freqMap.items()]
        heapq.heapify(maxHeap)
        res = []
        prev = ''

        while maxHeap:
            # take the most freq key in the map that is not prev
            print(f'heap: {maxHeap} res: {res} prev: {prev}')
            candidate = ''
            maxFreq, maxStr = heapq.heappop(maxHeap)
            if maxStr == prev and len(maxHeap) == 0:
                return ''
            
            if maxStr == prev and len(maxHeap) > 0:
                secondMax, secondStr = heapq.heappop(maxHeap)
                candidate = secondStr
                heapq.heappush(maxHeap, (maxFreq, maxStr))
                if secondMax + 1 < 0:
                    heapq.heappush(maxHeap, (secondMax + 1, secondStr))
            else:
                candidate = maxStr
                if maxFreq + 1 < 0:
                    heapq.heappush(maxHeap, (maxFreq + 1, maxStr))
            if not candidate:
                return ''
            prev = candidate
            res.append(candidate)
        print(prev)
        return ''.join(res)