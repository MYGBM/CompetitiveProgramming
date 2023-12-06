class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxGoodInt=""
       
        for i in range(len(num)-2):
            
            if num[i]==num[i+1]==num[i+2]:
               
                tempGoodInt=num[i]*3
                
                if tempGoodInt > maxGoodInt:
                    print(tempGoodInt)
                    maxGoodInt=tempGoodInt
               
        return(maxGoodInt)
       