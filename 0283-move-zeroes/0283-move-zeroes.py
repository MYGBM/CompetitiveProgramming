class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer1 = 0  # seeking pointer
        pointer2 = 0  # placeholder pointer to place non-zero elements
        
        while pointer1 < len(nums):
            if nums[pointer1] != 0:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer2 += 1
            pointer1 += 1



        """
        Do not return anything, modify nums in-place instead.
        """
        