import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #convert array to integer
        num=int(''.join(str(x) for x in num))
        sum=k+num
        sum=list(map(int,str(sum)))
        return sum
        
