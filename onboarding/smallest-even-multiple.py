class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i = 1
        while True:
            multiple = n*i
            if  multiple%2==0:
                return multiple
                break
            i+=1
                
            
                
        