class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        frequency=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    frequency+=1
        return frequency
                
        