class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        while start < end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid+1
            else:
                end = mid
        if nums[start]==target:
            return start
        else:
            return -1
            



        