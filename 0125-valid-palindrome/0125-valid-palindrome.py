class Solution:
    def isPalindrome(self,s: str) -> bool:
        leftPointer=0
        rightPointer=len(s)-1
        while leftPointer<rightPointer:
            # skip over non alphaNumeric characters
            while leftPointer<rightPointer and not self.alphaNum(s[leftPointer]):
                leftPointer+=1
            while rightPointer>leftPointer and not self.alphaNum(s[rightPointer]):
                rightPointer-=1

            #condition 
            if s[leftPointer].lower()!=s[rightPointer].lower():
                return False 

            #increment the values of the pointers
            leftPointer+=1
            rightPointer-=1
        return True


    # custom alphaNum function inPlace 
    def alphaNum(self,character):
        return(ord("A")<=ord(character)<=ord("Z") or ord("a")<=ord(character)<=ord("z") or ord("0")<=ord(character)<=ord("9"))
           



        