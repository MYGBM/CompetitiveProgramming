class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        tempCount = 0
        for i in range(len(nums)): 
            
            if nums[i]==0:
                count = max(tempCount, count)
                tempCount = 0
                
            else:
                tempCount += 1
                
        # handling case for ending with a 1
        count = max(tempCount, count)
                
            
                    
        return count
            
                
                
        