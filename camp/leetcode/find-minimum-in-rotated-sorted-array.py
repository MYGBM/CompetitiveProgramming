class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        low = 0
        high = len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>=last:
                low=mid+1
            else:
                high = mid
            print(low)
        return(nums[low])