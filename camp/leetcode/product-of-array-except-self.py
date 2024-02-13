class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = []
        left_array = []
        l = 1
        for i in range(len(nums)):
            left_array.append(l)
            l *= nums[i]

        right_array = [0 for _ in range(len(nums))]
        r = 1
        for i in range(len(nums)-1,-1,-1):
            print(i)
            right_array[i] = r
            r *= nums[i]
        
        for i in range(len(nums)):
            soln.append(left_array[i] * right_array[i])
        
        return soln
            
    





