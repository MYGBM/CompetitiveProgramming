class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            tempstrs=[]
            for row in range(len(strs)):
                tempstrs.append(strs[row][col])

            sortedTemp = sorted(tempstrs)
            if sortedTemp!=tempstrs:
                count +=1
        return count


        