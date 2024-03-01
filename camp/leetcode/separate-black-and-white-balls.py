class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0 #always count idx2-idx1
        idx = len(s)-1 #create a partition to place the ones at the end
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                count+=abs(i-idx)
                idx-=1
        return count
