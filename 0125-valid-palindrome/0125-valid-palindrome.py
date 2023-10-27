class Solution:
    def isPalindrome(self,s: str) -> bool:
       

        #AUxiliary space 0(n) 
        newS="".join(c for c in s if c.isalnum())
        newS=newS.lower()
        
        #initializing left and rightPointers
        leftPointer=0
        rightPointer=len(newS)-1

        while leftPointer<len(newS) and rightPointer>0:
            if newS[leftPointer]!=newS[rightPointer]:
                return False 

            #increment the values of the pointers
            leftPointer+=1
            rightPointer-=1
        return True

           



        