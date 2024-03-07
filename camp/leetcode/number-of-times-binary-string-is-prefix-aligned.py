class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi = -inf
        count = 0
        ans =0
        for i in range(len(flips)):
            maxi = max(maxi,flips[i])
            count+=1
            if maxi==count:
                ans+=1
        return ans
        