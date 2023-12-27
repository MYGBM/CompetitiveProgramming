class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        #Approach2 Optimized Way
        sorted_nums = sorted(nums) 
        print(sorted_nums)
        nums_to_idx = {} 

        for idx,val in enumerate(sorted_nums):
            if val in nums_to_idx:
                continue
            nums_to_idx[val] = idx

        for idx in range(len(nums)):
            nums[idx] = nums_to_idx[nums[idx]]
        
        return nums
        
        