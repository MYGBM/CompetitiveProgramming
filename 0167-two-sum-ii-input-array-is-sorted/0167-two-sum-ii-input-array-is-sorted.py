class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointerLeft=0
        pointerRight=len(numbers)-1
        
        while pointerLeft<len(numbers) and pointerRight>0: # Time complexity 0(N)
            if numbers[pointerLeft]+numbers[pointerRight]==target:
                return [pointerLeft+1,pointerRight+1]
            elif numbers[pointerLeft]+numbers[pointerRight]<target:
                pointerLeft+=1
            elif numbers[pointerLeft]+numbers[pointerRight]>target:
                pointerRight-=1
            else:
                return []
        
        