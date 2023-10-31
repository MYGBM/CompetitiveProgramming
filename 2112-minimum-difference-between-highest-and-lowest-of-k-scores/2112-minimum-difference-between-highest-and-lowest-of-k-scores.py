class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #sort the array so as to find the smallest difference
        nums.sort() #Time complexity nlogn
        #initialize the pointers
        l,r=0,k-1

        #maximum difference set to infinity
        res=float("inf")

        #set up the pointer condition
        while r<len(nums): #0(N) time complexity
            res=min(res,nums[r]-nums[l])
            #increment the pointers
            l,r=l+1,r+1
        return res



    