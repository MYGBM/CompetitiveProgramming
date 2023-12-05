class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = { word : index for index, word in enumerate(order)}
        
        
        for i in range(len(words)-1):
            
            j = 0
            
            
            while j<len(words[i]) and j<len(words[i+1]):
                flag = 0
              # check words[i][j] and words[i+1][j] in each iteration
            
            
            
                if words[i][j] != words[i+1][j] and orderDict[words[i][j]] < orderDict[words[i+1][j]]:
                    flag = 1
                    
                    break 
                    
                    
        
               
                #handle the case when there is an inequality and order fails 
                elif  words[i][j] != words[i+1][j] and orderDict[words[i][j]] > orderDict[words[i+1][j]]:
                    return False
                
                elif words[i][j] == words[i+1][j]:
                    j += 1
                    
            
            if len(words[i]) > len(words[i+1]) and flag == 0:
                return False
                
                # handle case when a word is a subword of another
                    
                

        return True
                
            
            
                
                
        
            
        
        