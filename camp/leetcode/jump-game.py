class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums)-1
        i = len(nums)-1

        while i > -1:

            if nums[i] + i >=good:
                good = i
            i-=1

        return good==0


        