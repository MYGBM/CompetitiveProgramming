class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPointer = 0
        rightPointer = len(s)-1
        while leftPointer < rightPointer:
            s[leftPointer],s[rightPointer] = s[rightPointer],s[leftPointer]
            leftPointer += 1
            rightPointer -= 1
        
        
        