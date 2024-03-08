class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        hashMap = {}
        total_zeros = nums.count(0)
        total_ones = nums.count(1)
        zero_left = 0
        n = len(nums)
        ans =[]
        for i in range(n+1):
            if i==0:
                score = total_ones
            if i==n+1:
                score = total_zeros
            else:
                if nums[i-1]==0:
                    zero_left+=1
                else:
                    total_ones-=1
                score = zero_left+total_ones
            hashMap[i]=score

        
        maxi = max(hashMap.values())
        for key in hashMap:
            if hashMap[key] == maxi:
                ans.append(key)
        
        return ans




        