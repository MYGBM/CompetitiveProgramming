class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        hashMap = {0:1}
        total_count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in hashMap:
                total_count += hashMap[curr_sum-k]

            hashMap[curr_sum] = hashMap.get(curr_sum,0) + 1
    
        
        return total_count
