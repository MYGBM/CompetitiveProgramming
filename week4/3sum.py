class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = set()
        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                if nums[left] +nums[right] +nums[i] == 0:
                    soln.add(tuple([nums[i],nums[left],nums[right]]))
                    left +=1
                    right -=1
                    
                elif nums[left] +nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] +nums[right] +nums[i] > 0:
                    right -= 1
                
                
        
        return list(soln)


        