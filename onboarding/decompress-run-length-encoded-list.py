class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        
        
        i = 0
        while i<len(nums)-1:
            temp = []
            if nums[i+1]<=9:
                temp = str(nums[i+1])*nums[i]
                temp = list(temp)
                
            elif nums[i+1]<=99:
                temp = str(nums[i+1])*nums[i]
                temp =[temp[i:i+2] for i in range(0,len(temp),2)]
                
            else:
                temp = str(nums[i+1])*nums[i]
                temp =[temp[i:i+3] for i in range(0,len(temp),3)]
                
            output.extend(temp)
            
            
            i += 2
            
        output=[int(o) for o in output]
        
        return output
        
        
        