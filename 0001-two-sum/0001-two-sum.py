class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i,num in enumerate(nums) :
             secondNum=target-num
             if secondNum in nums[i+1:]:
                 j=nums[i+1:].index(secondNum)+i+1
                 return(i,j)


        
