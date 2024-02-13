class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = nums[0]
        ans = []
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append(curr_sum+nums[i])
            curr_sum += nums[i]
    
        return ans 

