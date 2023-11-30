class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num//3
        rem = num%3
        
        if rem!=0:
            return []
        
        return [x-1,x,x+1]