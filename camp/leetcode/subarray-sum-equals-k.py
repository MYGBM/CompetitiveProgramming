class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        total_count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in hashMap:
                total_count += hashMap[curr_sum-k]

            hashMap[curr_sum] = hashMap.get(curr_sum,0) + 1
    
        
        return total_count








        