class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        mini = 10**6
        total = 0
        

        for right in range(len(nums)):
            total += nums[right]

            while total >=target:
                mini = min(mini,right-left+1)
                total -= nums[left]
                left+=1
            
        return 0 if mini==10**6 else mini
                
            
        