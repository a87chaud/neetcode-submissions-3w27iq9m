class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqMap = defaultdict(int)
        for h in hand:
            freqMap[h] += 1
        minHeap = list(freqMap.keys())
        heapq.heapify(minHeap)
        print(minHeap)
        while minHeap:
            minStart = minHeap[0]
            end = minStart + groupSize
            for i in range(minStart, end):
                if i not in freqMap:
                    return False
                freqMap[i] -= 1
                if freqMap[i] <= 0:
                    del freqMap[i]
                    continue
            minHeap = list(freqMap.keys())
            heapq.heapify(minHeap)
        return True