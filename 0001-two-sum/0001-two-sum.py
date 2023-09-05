class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            end=len(nums)
            for i in range(0,end) :
                for j in range(i+1,end):
                    if nums[i]+nums[j]==target:
                        return(i,j)


        
