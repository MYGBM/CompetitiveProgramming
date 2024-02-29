class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        maxi = -inf
        unique_sum = 0
        elem = set()

        for right in range(len(nums)):
            while nums[right] in elem:
                unique_sum -= nums[left]
                elem.remove(nums[left])
                left+=1

            
            unique_sum+=nums[right]
            elem.add(nums[right])
            print(unique_sum)
             
            
           

            # print(unique_sum)
            maxi = max(maxi,unique_sum)
        
        return maxi

        