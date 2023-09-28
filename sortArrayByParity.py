class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        newArr=[]
        for i in nums:
            if i%2==0:
                newArr.append(i)
        for i in nums:
            if i%2!=0:
                newArr.append(i)
        return newArr
        
