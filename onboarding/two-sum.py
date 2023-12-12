class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = []
        
        for i in range(len(nums)):
            newNums.append((nums[i],i))
            
        # print(newNums)
        
        newNums.sort()
        
        pointer1 = 0
        pointer2 = len(nums)-1
        
        while pointer1 < pointer2:
            if newNums[pointer1][0]+newNums[pointer2][0] < target:
                pointer1 += 1
                
            elif newNums[pointer1][0]+newNums[pointer2][0] > target:
                pointer2 -= 1
                
            elif newNums[pointer1][0]+newNums[pointer2][0] == target:
                return [newNums[pointer1][1],newNums[pointer2][1]]
            
        
        

        
        
        
         