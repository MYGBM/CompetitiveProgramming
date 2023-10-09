class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
         
        heightToName={}
        for height,name in zip(heights,names):
            heightToName[height]=name

        n=len(heights)
        for i in range(1,n):
            key=heights[i]
            j=i-1
            while j>=0 and heights[j]<key:
                heights[j+1]=heights[j]
                j-=1
                heights[j+1]=key
            
        #map the sorted height back to the names
        names_list=[]
        for height in heights:
            names_list.append(heightToName[height])
        return names_list

#problem insertion sort is supposed to be in place 
        
