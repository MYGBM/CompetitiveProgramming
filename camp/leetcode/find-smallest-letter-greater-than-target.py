class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def isGreater(char):
            return ord(char)>ord(target)
        low = 0
        high = len(letters)-1
        while low<high:
            mid = (low+high)//2
            if isGreater(letters[mid]):
                high =mid
            else:
                low = mid+1
        return letters[low] if isGreater(letters[low]) else  letters[0]
