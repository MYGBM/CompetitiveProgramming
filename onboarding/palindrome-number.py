class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #handling edge case
        
        if x<0:
            return False 
        #use variables temp and remainder
        temp = x
        res = 0
        
        while temp>=10:
            rem = temp%10
            res = res*10 +rem
            temp = temp//10
            
            
        res = res*10 + temp
        
        return(res==x)
    
        
        
        
                
        
            
        
        