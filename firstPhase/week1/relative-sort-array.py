class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        outPut1=[]
        outPut2=[]
        for i in arr2:
            for j in arr1:
                if j==i:
                    outPut1.append(j)
        
        for i in arr1:            
            if i not in arr2:
                    outPut2.append(i)

        return outPut1 + sorted(outPut2)
                
        