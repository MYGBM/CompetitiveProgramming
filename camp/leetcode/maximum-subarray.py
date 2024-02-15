class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        pos_flag = 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos_flag = 1
            curr += nums[i]
            if curr < 0:
                prefix.append(0)
                curr = 0
            else:
                prefix.append(curr)
        
       
        if pos_flag:
           return max(prefix)
        else:
            return max(nums)




        