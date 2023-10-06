class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targ_indices=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                targ_indices.append(i)
        return targ_indices