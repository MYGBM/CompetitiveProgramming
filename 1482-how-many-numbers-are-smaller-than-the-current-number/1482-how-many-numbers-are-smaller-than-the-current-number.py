class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index=len(nums)
        new=[0]*(index)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    new[i]+=1
        return(new)

        









                      