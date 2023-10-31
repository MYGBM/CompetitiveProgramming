class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>=len(nums):
            k=k%len(nums)    
        def reverse(leftPointer,rightPointer):
            while leftPointer<rightPointer:
                nums[leftPointer],nums[rightPointer]=nums[rightPointer],nums[leftPointer]
                leftPointer+=1
                rightPointer-=1
       
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)


        