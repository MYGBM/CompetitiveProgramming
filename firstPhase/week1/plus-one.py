class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = "".join(map(str,digits))
        integer = list(map(int,list(str(int(integer) +1))))
        return integer
        
    

        