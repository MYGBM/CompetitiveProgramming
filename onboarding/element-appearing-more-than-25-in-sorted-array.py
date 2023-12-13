class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        frequency = Counter(arr)
        max_frequency = max(frequency.values())
        return [key for key,value in frequency.items() if value==max_frequency][0]
        
        
        