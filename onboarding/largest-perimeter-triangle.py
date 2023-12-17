class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        [a,b,c,d,e,f,g,h]
                   i j k
        """
        nums.sort()
        for i in range(len(nums)-3, -1,-1):
            j = i+1
            k = i+2
            if nums[i]+nums[j]>nums[k]:
                return nums[i] + nums[j] + nums[k]
        
        return 0

         