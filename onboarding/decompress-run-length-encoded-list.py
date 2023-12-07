class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed =[]
        
        for i in range(len(nums)//2):
            tempDecompressed=[]
            freq, val = nums[2*i], [nums[2*i+1]]
            tempDecompressed = val * freq
            decompressed +=tempDecompressed
        
        return decompressed
            
            
            
        
        
            