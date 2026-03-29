class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        infected = set()
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                infected.add(i-1)
                infected.add(i)
                infected.add(i+1)
        for i in range(len(flowerbed)):
            if i not in infected:
                n -= 1
                infected.add(i + 1)
        
        return n <= 0
            