class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        print(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] +nums[i] > nums[i]+nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        print(nums)

        return str(int("".join(nums)))
        
        



        