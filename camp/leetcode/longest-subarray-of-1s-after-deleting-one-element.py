class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left= 0
        maxi_length = 0
        zero_count = 0


        for right in range(len(nums)):

            if nums[right]==0:
                zero_count +=1
        
            while zero_count>1:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            maxi_length= max(maxi_length,right-left)
           

        return maxi_length


        
        