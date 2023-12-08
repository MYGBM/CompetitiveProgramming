class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        hashMap = set()
        
        for i in range(len(ranges)):
             for x in range(ranges[i][0],ranges[i][-1]+1):
                    hashMap.add(x)
        
        for i in range(left,right+1):
                if i not in hashMap:
                    return False
                    
        return True
                    
            


                    
        
      