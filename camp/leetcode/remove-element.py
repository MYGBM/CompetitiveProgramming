class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pointer1 = 0  # seeking pointer
        pointer2 = 0  # placeholder pointer to place non-zero elements
        count =0
        while pointer1 < len(nums):
            if nums[pointer1] !=val :
                count+=1
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer2 += 1
            pointer1 += 1
        

        return count
            
                
        



      



        