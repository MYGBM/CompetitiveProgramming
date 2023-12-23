class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums = []
        negativeNums = []
        outPut = []
        pointerPositive = 0
        pointerNegative = 0
        # [3,1,2]  and [-2,-5,-4]
        #[3,-2,1,-5,2,-4]
        for num in nums:
            if num>0:
                positiveNums.append(num)
            else:
                negativeNums.append(num)
        while pointerPositive < len(positiveNums):
            outPut.append(positiveNums[pointerPositive])
            outPut.append(negativeNums[pointerNegative])
            pointerPositive+=1
            pointerNegative+=1
        return outPut
        


        