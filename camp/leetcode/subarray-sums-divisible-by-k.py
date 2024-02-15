class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        ans = 0
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum%k in hashMap:
                ans += hashMap[curr_sum%k]
                hashMap[curr_sum%k] += 1
            else:
                hashMap[curr_sum%k] = 1
        
        return ans
            