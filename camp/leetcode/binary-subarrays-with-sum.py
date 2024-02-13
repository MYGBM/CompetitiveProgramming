class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = {0:1}
        total_count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - goal in hashMap:
                total_count += hashMap[curr_sum-goal]

            hashMap[curr_sum] = hashMap.get(curr_sum,0) + 1
    
        
        return total_count

