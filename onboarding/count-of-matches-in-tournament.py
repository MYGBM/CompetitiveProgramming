class Solution:
    def numberOfMatches(self, n: int) -> int:
        output = 0
        while n != 1:
            if n% 2==0:
                output += n//2 # add the matches 
                n = n//2 # the advance
            
            else:
                output +=(n-1)//2 #add the matches
                n = ((n-1)//2) +1 #the advance
        return output
            
                
            





        