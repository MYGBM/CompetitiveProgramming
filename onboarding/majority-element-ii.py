class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        frequency = Counter(nums)
        n = len(nums)
        
        return [key for key,value in frequency.items() if value>n/3] 
        