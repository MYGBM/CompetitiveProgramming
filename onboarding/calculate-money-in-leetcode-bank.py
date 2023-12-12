class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        remain= n%7
        start = 1
        stop = 7
        output =0
        
        if n <7:
            for i in range(1,remain+1):
                output += i
        else:
            for i in range(weeks):
                for i in range(start,stop+1):
                    output +=i
                start+=1
                stop+=1
                
            # add the remaining elements
            for i in range(start,start+remain):
                output += i
        
        return output
        
        
                
        
        
        
        
        