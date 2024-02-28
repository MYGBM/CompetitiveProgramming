class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        maxi_length = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1

            if zero_count >k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            maxi_length = max(maxi_length,right-left+1)
        
        return maxi_length

        