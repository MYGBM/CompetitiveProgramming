class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        leftPointer = 0
        rightPointer = n
        output =[]
        
        while rightPointer<n*2:
            output.append(nums[leftPointer])
            output.append(nums[rightPointer])
            leftPointer+=1
            rightPointer+=1
        
        return output
        
            
        