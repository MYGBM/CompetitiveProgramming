class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequency={} #auxiliary O(n)
        solution=[] #auxiliary O(n)

        for items in arr1: #Time complexity O(n)
            if items not in frequency:
                frequency[items]=0
            frequency[items]+=1
        
        #Time complexity O(k)
        #For appending the items 
        for items in arr2:
            count=frequency[items]
            if count!=0:
                solution.extend([items]*count)
                frequency.pop(items)
        
        #sort the remaining items
        #Time complexity O(nlogn)
        remaining=sorted(frequency.keys())
        for items in remaining: #Time complexity 0(n-k)
            solution.extend([items]*frequency[items])
        return solution


#Time O(n+k+nlogn)
#Space O(n)
            


        