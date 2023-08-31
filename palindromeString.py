class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=""
        for char in s:
            if char.isalnum():
                newS+=char
        newS=newS.lower()
        return newS[::-1]==newS
