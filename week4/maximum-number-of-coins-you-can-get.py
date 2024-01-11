class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort()
        start = len(piles)-2
        stop = len(piles)//3 -1

        for i in range(start,stop,-2):
            count += piles[i]
        return count

        