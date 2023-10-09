class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length=len(names)
        for i in range(length):
            for j in range(i+1,length):
                if heights[j]>heights[i]:
                    heights[j],heights[i]=heights[i],heights[j]
                    names[j],names[i]=names[i],names[j]
        return names 
                    


        
