class Solution:
    def reverseWords(self, s: str) -> str:
        newS = s.split()
        newS = " ".join(reversed(newS))
        return newS