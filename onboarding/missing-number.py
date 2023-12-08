class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        interval = set()
        fullInterval = set([x for x in range(0,len(nums)+1)])
        missingInterval = set(nums)
        
        differenceSet = fullInterval - missingInterval
        differenceSet = (list(differenceSet))[0]
        
        
        return differenceSet
        
        
        