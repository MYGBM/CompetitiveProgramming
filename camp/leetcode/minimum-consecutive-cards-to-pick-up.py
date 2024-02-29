class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        hashMap = defaultdict(int)
        mini = inf

        for right in range(len(cards)):
            hashMap[cards[right]]+=1

            while hashMap[cards[right]] >1:
                mini = min(mini,right-left+1)
                hashMap[cards[left]]-=1
                left+=1

        if mini==inf:
            return -1
        else:
            return mini

                


        