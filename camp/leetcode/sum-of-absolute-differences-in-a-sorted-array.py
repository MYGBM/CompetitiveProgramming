class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        soln = []
        prefix_sum = [0 for i in range(len(nums))]
        prefix_sum[0] = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        print(prefix_sum)

        for i in range(len(prefix_sum)):
            left = ((i+1)*nums[i]) - (prefix_sum[i])
            right = (nums[i]*(-n+i+1))+ (prefix_sum[-1] - prefix_sum[i])
            soln.append(left+right)

        return soln       
        

        
        
        
        

        

        
        