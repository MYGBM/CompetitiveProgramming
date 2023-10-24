class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPointer=1 #AuxiliarySpace 0(1)
        for rightPointer in range(1,len(nums)): #AuxiliarySpace 0(1)
            # #Non unique case
            # if nums[rightPointer]==nums[rightPointer-1]
            # rightPointer+=1
            #Already taken care of by the for loop

            #Unique case
            if nums[rightPointer]!=nums[rightPointer-1]:
                nums[leftPointer]=nums[rightPointer]
                leftPointer+=1
        return leftPointer



             






        