class Solution:
    def interpret(self, command: str) -> str:
        
        left_ptr = 0
        right_ptr = 1
        output = ""
        
        while left_ptr<len(command):
            if command[left_ptr]=="G":
                output += "G"
                left_ptr += 1
                right_ptr += 1
            
            elif command[right_ptr]==")":
                output += "o"
                left_ptr += 2
                right_ptr += 2
            
            else:
                output += "al"
                left_ptr += 4
                right_ptr += 4
            
        return output
            
            

            
            
    
         
        
        
        
        
        
        
        
        
        
        
        
        