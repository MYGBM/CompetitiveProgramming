class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashMap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
        output = 0
                    
        for i in range(len(s),-1,-1):
            
            #handling index out of bound case
            
            if i==len(s)-1:
                output+=hashMap[s[i]]

            elif i<len(s)-1 and hashMap[s[i+1]] <= hashMap[s[i]]:
                output += hashMap[s[i]]

            elif i < len(s)-1 and hashMap[s[i+1]]> hashMap[s[i]]:
                output -= hashMap[s[i]]


        
        return output
            
        

            
                
    
                
            
            
        
        
        
        
        
        