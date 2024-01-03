class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        firstPointer = 0
        secondPointer = 1
        for i in range(len(nums)):
            if firstPointer<len(nums) and secondPointer<len(nums):
                if nums[secondPointer] == nums[firstPointer]:
                        nums[secondPointer] = 101
                        secondPointer += 1
                   
                else:
                    firstPointer = secondPointer
                    secondPointer = firstPointer + 1
            else:
                break

        holder = 0
        seeker = 0
        while seeker <len(nums):
            if nums[seeker]!=101:
                nums[holder],nums[seeker] = nums[seeker],nums[holder]
                holder +=1
            seeker +=1

        for i in range(len(nums)):
            if nums[i]==101:
                return i

        

        
                
            



        