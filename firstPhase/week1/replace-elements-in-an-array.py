class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        
        for i, j  in  operations:
            nums[dic[i]] = j
            dic[j] = dic.pop(i)
            
        return nums
        